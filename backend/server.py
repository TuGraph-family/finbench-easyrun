from flask import Flask
import logging

app = Flask(__name__)

logger = app.logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
for handler in logger.handlers:
    handler.setFormatter(formatter)

current_dataset = None
current_task = None
current_output = None

validated = False
benchmarked = False

RESPONSE_OK = {'status':'ok', 'message': ''}
RESP_FAILED_TMPL = {'status':'failed'}