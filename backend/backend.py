#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project : finbench-easyrun 
@File    : backend
'''

from flask import Flask, request
from flask_cors import CORS
import utils
import os
import server

app = Flask(__name__)
CORS(app, resources=r"/*")

RESPONSE_OK = {"status": "ok", "message": ""}
RESP_FAILED_TMPL = {"status": "failed", "message": ""}

def wrap_data(resp: dict):
    return {'data': resp}

@app.route('/list_dataset', methods=['POST'])
def list_dataset():
    datasets = []
    dirs = os.listdir("../datasets/")
    if 'sf1' in dirs:
        datasets.append('sf1')
    if 'sf10' in dirs:
        datasets.append('sf10')
    return wrap_data({'datasets': datasets})


@app.route('/load_dataset', methods=['POST'])
def load_dataset():
    dataset = request.json.get('dataset')
    server.logger.info('Loading dataset: {}'.format(dataset))
    if dataset is None or dataset not in ['sf1', 'sf10']:
        return RESP_FAILED_TMPL.update({'message': 'Invalid dataset name'})
    global current_dataset
    current_dataset = dataset
    logs = utils.load_dataset(dataset)
    import_res = logs[-1].strip()
    if 'Import finished' in import_res:
        return RESPONSE_OK
    else:
        return RESP_FAILED_TMPL.update({'message': import_res})
        

@app.route('/start_sut', methods=['POST'])
def start_sut():
    global current_dataset
    if current_dataset is None:
        return {'status':'failed', 'message': 'No dataset loaded'}
    logs = utils.start_tugraph(current_dataset)
    start_res = logs[-1].strip()
    if 'The service process is started at' in start_res:
        return RESPONSE_OK
    else:
        return RESP_FAILED_TMPL.update({'message': start_res})


@app.route('/start_test', methods=['POST'])
def start_test():
    global current_dataset
    if current_dataset is None:
        return RESP_FAILED_TMPL.update({'message': 'No dataset loaded'})
    mode = request.args.get('mode')
    if mode == 'validate':
        if current_dataset != 'sf1':
            msg = 'Validation only supports sf1. Current dataset is {}'.format(current_dataset)
            return RESP_FAILED_TMPL.update({'message': msg})
        succeed, msg = utils.start_validate()
        if succeed:
            return RESPONSE_OK.update({'message': msg})
        else:
            server.logger.error(msg)
            return RESP_FAILED_TMPL.update({'message': msg})
    elif mode == 'benchmark':
        # if current_dataset != 'sf10':
        #     msg = 'Benchmark only supports sf10. Current dataset is {}'.format(current_dataset)
        #     return RESP_FAILED_TMPL.update({'message':  msg})
        # logs = utils.start_benchmark()
        return RESPONSE_OK
    else:
        return RESP_FAILED_TMPL.update({'message': 'Invalid mode'})


@app.route('/progress', methods=['POST'])
def progress():
    global current_task
    if current_task is None:
        return RESP_FAILED_TMPL.update({'message': 'No task running'})
    line = current_task.readline()
    server.logger.info(line)
    return RESPONSE_OK


@app.route('/result', methods=['POST'])
def result():
    return RESPONSE_OK


@app.route('/reset_all', methods=['POST'])
def reset_all():
    server.current_dataset = None
    server.validated = False
    server.benchmarked = False
    utils.stop_finbench_dockers()
    utils.start_finbench_dockers()
    return RESPONSE_OK


def server_init():
    utils.start_finbench_dockers()

    
def server_destroy():
    utils.stop_finbench_dockers()


if __name__ == '__main__':
    server_init()
    app.run(host='0.0.0.0', debug=True)
    server_destroy()
