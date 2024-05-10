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

current_dataset = None
validated = False
benchmarked = False

logger = app.logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
for handler in logger.handlers:
    handler.setFormatter(formatter)