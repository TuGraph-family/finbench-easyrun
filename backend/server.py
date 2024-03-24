#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：finbench-easyrun 
@File    ：server
'''

from flask import Flask

import utils
import os

app = Flask(__name__)

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
    return 'Welcome to the Flask Demo!'

@app.route('/start_sut')
def start_sut():
    return 'Welcome to the Flask Demo!'

@app.route('/start_test')
def start_test():
    return 'Welcome to the Flask Demo!'

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

