import os
import subprocess
import docker

client = docker.from_env()

DOCKER_PREFIX = "finbench-easyrun"
FINBENCH_DOCKER = "{}_finbench_1".format(DOCKER_PREFIX)
TUGRAPH_DOCKER = "{}_tugraph_1".format(DOCKER_PREFIX)

def check_docker(name):
    return client.containers.list(filters={'name': name})

def stop_finbench_dockers():
    os.system('docker-compose -f ../docker-compose.yml down')

def start_finbench_dockers():
    # if check_docker(FINBENCH_DOCKER) or check_docker(TUGRAPH_DOCKER):
    #     stop_finbench_dockers()
    if check_docker(FINBENCH_DOCKER) and check_docker(TUGRAPH_DOCKER):
        return
    os.system('docker-compose -f ../docker-compose.yml up -d')
    
def load_dataset(dataset):
    cmd_tmpl = 'docker exec -it {} bash /root/scripts/{}_import.sh'
    output = subprocess.run(cmd_tmpl.format(TUGRAPH_DOCKER, dataset), capture_output=True, shell=True, text=True)
    return output.stdout.splitlines()

def start_tugraph(dataset):
    cmd_tmpl = 'docker exec -it {} bash /root/scripts/{}_start.sh'
    output = subprocess.run(cmd_tmpl.format(TUGRAPH_DOCKER, dataset), capture_output=True, shell=True, text=True)
    return output.stdout.splitlines()