#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：finbench-easyrun 
@File    ：server
'''

from flask import Flask, request

import utils
import os
import subprocess

app = Flask(__name__)

current_dataset = None

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
        return {'status':'failed', 'message': 'Invalid dataset name'}
    global current_dataset
    current_dataset = dataset
    logs = utils.load_dataset(dataset)
    import_res = logs[-1].strip()
    if 'Import finished' in import_res:
        return {'status':'ok', 'message': ''}
    else:
        return {'status':'failed', 'message': '{}'.format(import_res)}
        

@app.route('/start_sut')
def start_sut():
    global current_dataset
    if current_dataset is None:
        return {'status':'failed', 'message': 'No dataset loaded'}
    logs = utils.start_tugraph(current_dataset)
    start_res = logs[-1].strip()
    if 'The service process is started at' in start_res:
        return {'status':'ok', 'message': ''}
    else:
        return {'status':'failed', 'message': '{}'.format(start_res)}

@app.route('/start_test')
def start_test():
    global current_dataset
    mode = request.args.get('mode')
    if mode == 'validate':
        if current_dataset != 'sf1':
            return {'status':'failed', 'message': 'Validation test only supports sf1 dataset. Current dataset is {}'.format(current_dataset)}
        utils.start_validate()
        return 'Welcome to the Flask Demo!'
    elif mode == 'benchmark':
        if current_dataset != 'sf10':
            return {'status':'failed', 'message': 'Benchmark test only supports sf10 dataset. Current dataset is {}'.format(current_dataset)}
        utils.start_benchmark()
        return 'Welcome to the Flask Demo!'
    else:
        return {'status':'failed', 'message': 'Invalid test mode'}

@app.route('/progress')
def progress():
    return 'Welcome to the Flask Demo!'

@app.route('/result')
def result():
    return 'Welcome to the Flask Demo!'


def server_init():
    utils.start_finbench_dockers()
    
def server_destroy():
    utils.stop_finbench_dockers()

if __name__ == '__main__':
    server_init()
    app.run(debug=True)
    server_destroy()

