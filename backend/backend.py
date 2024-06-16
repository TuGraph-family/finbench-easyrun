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

WARMUP_PHASE = "Benchmarking TuGraph - Warmup Phase"
BENCHMARK_PHASE = "Benchmarking TuGraph - Benchmark Phase"

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
        server.target_ops = 10000
        thread = threading.Thread(target=run_validate)
        thread.start()
        return wrap_data({"status": "ok", "message": "", "uuid": task_id})
    elif mode == 'benchmark':
        op_count = request.json.get('ops')
        tcr = request.json.get('tcr')
        server.logger.info('start benchmark')
        server.current_mode = "benchmark"
        server.current_dataset = "sf10"
        server.target_ops = int(op_count)
        thread = threading.Thread(target=run_benchmark, args=(op_count, tcr))
        thread.start()
        return wrap_data({"status": "ok", "message": "", "uuid": task_id})
    else:
        return wrap_data(RESP_FAILED_TMPL.update({'message': 'illegal test mode'}))
    
def run_validate():
    server.current_status = 'Running'
    # load dataset sf1
    server.current_phase = "Loading dataset SF1"
    server.logger.info('Loading dataset sf1')
    logs = utils.load_dataset(server.current_dataset)
    import_res = logs[-1].strip()
    if 'Import finished' not in import_res:
        server.logger.error('Dataset loading failed: {}'.format(import_res))
        server.current_status = 'Failed'
        server.current_msg = import_res
    server.logger.info('sf1 Dataset loaded')
    
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
    
    # run validate
    server.current_phase = "Validating Results"
    server.async_process = utils.start_validate()
    server.logger.info('validation started')

def run_benchmark(op_count, tcr):
    server.current_status = 'Running'
    # load dataset sf10
    server.current_phase = "Loading dataset SF10"
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
    server.current_phase = "Benchmarking TuGraph"
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
                progress = round(processed * 100.0 / server.target_ops, 2)
                result['progress'] = progress
                if progress == 100.0:
                    result['status'] = 'Completed'
    return wrap_data(result)

def progress_benchmark():
    result = {}
    progress = 0.0
    log_file = "../scripts/benchmark_sf10.log"
    pattern = r"Runtime \[([^\]]+)\].*Operations \[([^\]]+)\].*Throughput \(Total\) \[([^\]]+)\]"
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.readlines()
            result['num_lines'] = len(logs)
            result['logs'] = logs[-300:]
            log300 = "\n".join(logs[-300:])
            log10 = "\n".join(logs[-10:])
            # Update the phase, find Run phase first
            if "Run Phase" in log300:
                server.current_phase = BENCHMARK_PHASE
            elif "Warmup Phase" in log300:
                server.current_phase = WARMUP_PHASE
            # find the metrics
            matches = re.findall(pattern, log300)
            if matches:
                last_match = matches[-1]
                operations = int(last_match[1].replace(',', ''))
                server.last_runtime = last_match[0]
                server.last_operations = operations
                throughput = round(float(last_match[2].replace(',', '')), 2)
                if throughput != 0.0:
                    server.last_throughput = throughput # skip the beginning of run phase
                if operations != 0:
                    target = server.target_ops / 4 if server.current_phase == WARMUP_PHASE else server.target_ops
                    server.last_progress = min(round(operations * 100.0 / target, 2), 100.0)
                    if "PASSED SCHEDULE AUDIT" in log10:
                        server.last_progress = 100.0
            # Update the status
            if "FAILED SCHEDULE AUDIT" in log300:
                server.current_status = 'Failed'
            if server.current_phase == BENCHMARK_PHASE and "Workload completed successfully" in log10 and "PASSED SCHEDULE AUDIT" in log10:
                server.last_progress = 100.0
                server.current_status = 'Completed'
    result['mode'] = server.current_mode
    result['dataset'] = server.current_dataset
    result['phase'] = server.current_phase
    result['status'] = server.current_status
    result['operations'] = server.last_operations
    result['throughput'] = server.last_throughput
    result['runtime'] = server.last_runtime
    result['progress'] = server.last_progress
    return wrap_data(result)


@app.route('/result', methods=['POST'])
def result():
    result_file = "../scripts/LDBC-FinBench-results.json"
    if os.path.exists(result_file):
        return wrap_data(open(result_file).read().strip())
    else:
        return wrap_data(RESP_FAILED_TMPL.update({'message': 'No result file'}))


@app.route('/reset_all', methods=['POST'])
def reset_all():
    server.current_mode = None
    server.current_dataset = None
    server.current_status = None
    server.current_phase = None
    server.current_msg = None
    server.last_operations = 0
    server.last_throughput = 0
    server.last_progress = 0.0
    server.last_runtime = "00:00:00"
    server.target_ops = None
    utils.stop_finbench_dockers()
    utils.start_finbench_dockers()
    utils.clean_log()
    return wrap_data(RESPONSE_OK)

# frontend static files
@app.route('/')
def serve_index():
    """Serve the index.html file."""
    return send_file('static/index.html')

@app.route('/assets/<path:path>')
def serve_static_files(path):
    """Serve static files."""
    return send_from_directory('static/assets', path)

@app.route('/<path:path>')
def catch_all(path):
    """Serve the index.html file for any other route to support SPA routing."""
    return send_file('static/index.html')


def server_init():
    utils.start_finbench_dockers()
    utils.clean_log()
    
    
def server_destroy():
    utils.stop_finbench_dockers()

if __name__ == '__main__':
    server_init()
    app.run(host='0.0.0.0', debug=True)
    server_destroy()
