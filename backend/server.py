#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project : finbench-easyrun 
@File    : server
'''
import logging
from backend import app

DOCKER_PREFIX = "finbench-easyrun"
FINBENCH_DOCKER = "{}_finbench_1".format(DOCKER_PREFIX)
TUGRAPH_DOCKER = "{}_tugraph_1".format(DOCKER_PREFIX)

current_mode = None
current_dataset = None
current_status = None
current_phase = None
current_msg = None
last_runtime = "00:00:00"
last_operations = 0
last_throughput = 0
last_progress = 0.0
target_ops = None
async_process = None

logger = app.logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
for handler in logger.handlers:
    handler.setFormatter(formatter)