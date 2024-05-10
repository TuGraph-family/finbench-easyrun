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
