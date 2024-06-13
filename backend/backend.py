#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project : finbench-easyrun 
@File    : backend
'''

from flask import Flask, request
from flask_cors import CORS
import os
import re
import utils
import server
import uuid
import threading

app = Flask(__name__)
CORS(app, resources=r"/*")

RESPONSE_OK = {"status": "ok", "message": ""}
RESP_FAILED_TMPL = {"status": "failed", "message": ""}

def wrap_data(resp: dict):
    return {'data': resp}

########################################################
# legacy interface
@app.route('/list_dataset', methods=['POST'])
def list_dataset():
    datasets = []
    dirs = os.listdir("../datasets/")
    if 'sf1' in dirs:
        datasets.append('sf1')
    if 'sf10' in dirs:
        datasets.append('sf10')
    return wrap_data({'datasets': datasets})

# legacy interface
@app.route('/load_dataset', methods=['POST'])
def load_dataset():
    dataset = request.json.get('dataset')
    server.logger.info('Dataset loading: {}'.format(dataset))
    if dataset is None or dataset not in ['sf1', 'sf10']:
        return wrap_data(RESP_FAILED_TMPL.update({'message': 'Invalid dataset name'}))
    server.current_dataset = dataset
    logs = utils.load_dataset(dataset)
    server.logger.info('Dataset loaded: {}'.format(dataset))
    import_res = logs[-1].strip()
    if 'Import finished' in import_res:
        return wrap_data(RESPONSE_OK)
    else:
        return wrap_data(RESP_FAILED_TMPL.update({'message': import_res}))
        
# legacy interface
@app.route('/start_sut', methods=['POST'])
def start_sut():
    if server.current_dataset is None:
        return wrap_data(RESP_FAILED_TMPL.update({'message': 'No dataset loaded'}))
    logs = utils.start_tugraph(server.current_dataset)
    start_res = logs[-1].strip()
    if 'The service process is started at' in start_res:
        return wrap_data(RESPONSE_OK)
    else:
        return wrap_data(RESP_FAILED_TMPL.update({'message': start_res}))
########################################################


@app.route('/start_test', methods=['POST'])
def start_test():
    mode = request.json.get('mode')
    task_id = str(uuid.uuid4())
    if mode == 'validate':
        server.logger.info('start validate')
        server.current_mode = "validate"
        server.current_dataset = "sf1"
        thread = threading.Thread(target=run_validate)
        thread.start()
        # run_validate()
        return wrap_data({"status": "ok", "message": "", "uuid": task_id})
    elif mode == 'benchmark':
        op_count = request.json.get('ops')
        tcr = request.json.get('tcr')
        server.logger.info('start benchmark')
        server.current_mode = "benchmark"
        server.current_dataset = "sf10"
        run_benchmark(op_count, tcr)
        return wrap_data({"status": "ok", "message": "", "uuid": task_id})
    else:
        return wrap_data(RESP_FAILED_TMPL.update({'message': 'illegal test mode'}))
    
def run_validate():
    server.current_status = 'Running'
    # load dataset sf1
    server.current_phase = "Loading dataset SF1..."
    server.logger.info('Loading dataset sf1')
    logs = utils.load_dataset(server.current_dataset)
    import_res = logs[-1].strip()
    if 'Import finished' not in import_res:
        server.logger.error('Dataset loading failed: {}'.format(import_res))
        server.current_status = 'Failed'
        server.current_msg = import_res
    server.logger.info('sf1 Dataset loaded')
    
    # start tugraph
    server.current_phase = "Starting TuGraph server..."
    server.logger.info('starting tugraph server')
    logs = utils.start_tugraph(server.current_dataset)
    start_res = logs[-1].strip()
    if 'The service process is started at' not in start_res:
        server.logger.error('TuGraph server start failed: {}'.format(start_res))
        server.current_status = 'Failed'
        server.current_msg = start_res
    server.logger.info('tugraph server started')
    
    # install procedures
    server.logger.info('installing procedures')
    logs = utils.install_procedures()
    server.logger.info('procedures installed')
    server.logger.info(logs)
    
    # run validate
    server.current_phase = "Validating Results..."
    server.async_process = utils.start_validate()
    server.logger.info('validation started')

def run_benchmark(op_count, tcr):
    server.current_status = 'Running'
    # load dataset sf1
    server.current_phase = "Loading dataset SF10.."
    server.logger.info('Loading dataset sf10')
    logs = utils.load_dataset(server.current_dataset)
    import_res = logs[-1].strip()
    if 'Import finished' not in import_res:
        server.logger.error('Dataset loading failed: {}'.format(import_res))
        server.current_status = 'Failed'
        server.current_msg = import_res
    server.logger.info('sf10 Dataset loaded')
    
    # start tugraph
    server.current_phase = "Starting TuGraph server"
    server.logger.info('starting tugraph server')
    logs = utils.start_tugraph(server.current_dataset)
    start_res = logs[-1].strip()
    if 'The service process is started at' not in start_res:
        server.logger.error('TuGraph server start failed: {}'.format(start_res))
        server.current_status = 'Failed'
        server.current_msg = start_res
    server.logger.info('tugraph server started')
    
    # install procedures
    server.logger.info('installing procedures')
    logs = utils.install_procedures()
    server.logger.info('procedures installed')
    server.logger.info(logs)
    
    # run benchmarking
    server.current_phase = "Benchmarking TuGraph..."
    server.async_process = utils.start_benchmark(op_count, tcr)
    server.logger.info('benchmarking started')


@app.route('/progress', methods=['POST'])
def progress():
    if server.current_mode == "validate":
        return progress_validate()
    elif server.current_mode == "benchmark":
        return progress_benchmark()
    else:
        return wrap_data(RESP_FAILED_TMPL.update({'message': 'Incorrect mode'}))

def progress_validate():
    result = {}
    result['mode'] = server.current_mode
    result['dataset'] = server.current_dataset
    result['phase'] = server.current_phase
    result['status'] = server.current_status
    result['progress'] = 0.0
    log_file = "../scripts/validate_sf1.log"
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.readlines()
            result['num_lines'] = len(logs)
            result['logs'] = logs[-300:]
            matches = re.findall(r"Processed ([\d,]+) / 10,000", "\n".join(logs[-300:]))
            if matches:
                last_match = matches[-1]
                processed = int(last_match.replace(',', ''))
                progress = round(processed / 100.0, 2)
                result['progress'] = progress
                if progress == 100.0:
                    result['status'] = 'Completed'
    return wrap_data(result)

def progress_benchmark():
    result = {}
    result['mode'] = server.current_mode
    result['dataset'] = server.current_dataset
    result['phase'] = server.current_phase
    result['status'] = server.current_status
    result['progress'] = 0.0
    log_file = "../scripts/benchmark_sf10.log"
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.readlines()
            result['num_lines'] = len(logs)
            result['logs'] = logs[-300:]
            matches = re.findall(r"Processed ([\d,]+) / 10,000", "\n".join(logs[-300:]))
            if matches:
                last_match = matches[-1]
                processed = int(last_match.replace(',', ''))
                progress = round(processed / 100.0, 2)
                result['progress'] = progress
                if progress == 100.0:
                    result['status'] = 'Completed'
    return wrap_data(result)


@app.route('/result', methods=['POST'])
def result():
    return wrap_data(RESPONSE_OK)


@app.route('/reset_all', methods=['POST'])
def reset_all():
    server.current_dataset = None
    server.current_mode = None
    server.current_msg = None
    server.current_phase = None
    server.current_status = None
    utils.stop_finbench_dockers()
    utils.start_finbench_dockers()
    utils.clean_log()
    return wrap_data(RESPONSE_OK)


def server_init():
    utils.start_finbench_dockers()
    utils.clean_log()
    
    
def server_destroy():
    utils.stop_finbench_dockers()
    utils.clean_log()

if __name__ == '__main__':
    server_init()
    app.run(host='0.0.0.0', debug=True)
    server_destroy()
