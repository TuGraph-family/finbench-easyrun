#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：finbench-easyrun 
@File    ：server
'''

from server import *
from flask import request
import utils
import os
import subprocess


@app.route('/list_dataset')
def list_dataset():
    datasets = []
    dirs = os.listdir("../datasets/")
    if 'sf1' in dirs:
        datasets.append('sf1')
    if 'sf10' in dirs:
        datasets.append('sf10')
    return {'datasets': datasets}


@app.route('/load_dataset')
def load_dataset():
    dataset = request.args.get('dataset')
    if dataset not in ['sf1', 'sf10']:
        return RESP_FAILED_TMPL.update({'message': 'Invalid dataset name'})
    global current_dataset
    current_dataset = dataset
    logs = utils.load_dataset(dataset)
    import_res = logs[-1].strip()
    if 'Import finished' in import_res:
        return RESPONSE_OK
    else:
        return RESP_FAILED_TMPL.update({'message': import_res})
        

@app.route('/start_sut')
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


@app.route('/start_test')
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
            logger.error(msg)
            return RESP_FAILED_TMPL.update({'message': msg})
    elif mode == 'benchmark':
        # if current_dataset != 'sf10':
        #     msg = 'Benchmark only supports sf10. Current dataset is {}'.format(current_dataset)
        #     return RESP_FAILED_TMPL.update({'message':  msg})
        # logs = utils.start_benchmark()
        return RESPONSE_OK
    else:
        return RESP_FAILED_TMPL.update({'message': 'Invalid mode'})


@app.route('/progress')
def progress():
    global current_task
    if current_task is None:
        return RESP_FAILED_TMPL.update({'message': 'No task running'})
    line = current_task.readline()
    logger.info(line)
    return RESPONSE_OK


@app.route('/result')
def result():
    return RESPONSE_OK


@app.route('/reset_all')
def reset_all():
    global current_dataset
    global validated
    global benchmarked
    current_dataset = None
    validated = False
    benchmarked = False
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
