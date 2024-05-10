from server import *
import os
import subprocess
import docker

DOCKER_PREFIX = "finbench-easyrun"
FINBENCH_DOCKER = "{}_finbench_1".format(DOCKER_PREFIX)
TUGRAPH_DOCKER = "{}_tugraph_1".format(DOCKER_PREFIX)

def check_docker(name):
    client = docker.from_env()
    return client.containers.list(filters={'name': name})

def stop_finbench_dockers():
    os.system('docker-compose -f ../docker-compose.yml down')

def start_finbench_dockers():
    if check_docker(FINBENCH_DOCKER) and check_docker(TUGRAPH_DOCKER):
        logger.warning('Docker containers already running.')
    else:
        os.system('docker-compose -f ../docker-compose.yml up -d')
    
def load_dataset(dataset):
    cmd = 'docker exec -it {} bash /root/scripts/{}_import.sh'.format(TUGRAPH_DOCKER, dataset)
    output = subprocess.run(cmd, capture_output=True, shell=True, text=True)
    return output.stdout.splitlines()

def start_tugraph(dataset):
    cmd = 'docker exec -it {} bash /root/scripts/{}_start.sh'.format(TUGRAPH_DOCKER, dataset)
    output = subprocess.run(cmd, capture_output=True, shell=True, text=True)
    return output.stdout.splitlines()

def start_validate():
    if validated:
        return False, 'Validation has been performed.'
    # load procedures first
    logs = load_procedure()
    if logs.count('200') == 4:
        logger.info('Procedures loaded successfully.')
    elif logs.count('200') == 8:
        logger.info('Procedures already loaded.')
    else:
        msg = 'Procedures loaded failed.'
        logger.error(msg + ' Reason: \n{}'.format(logs))
        return False, msg
    
    cmd = 'docker exec -it {} bash /root/scripts/sf1_validate.sh'.format(FINBENCH_DOCKER)
    global current_task
    current_task = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # logger.info(output.stdout[-20:])
    return True, 'submitted'

def start_benchmark():
    # load procedures first
    logs = load_procedure()
    if logs.count('200') == 4:
        logger.info('Procedures loaded successfully')
    elif logs.count('200') == 8:
        logger.info('Procedures already loaded.')
    else:
        msg = 'Procedures loaded failed.'
        logger.error(msg + ' Reason: \n{}'.format(logs))
        return False, msg
    return ""

def load_procedure():
    cmd = 'docker exec -it {} bash /root/scripts/load_procedure.sh'.format(FINBENCH_DOCKER)
    output = subprocess.run(cmd, capture_output=True, shell=True, text=True)
    return output.stdout.splitlines()
