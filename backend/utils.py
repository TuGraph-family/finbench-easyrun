import os
import docker

client = docker.from_env()

def check_docker(name):
    return client.containers.list(filters={'name': name})

def stop_finbench_dockers():
    os.system('docker-compose -f ../docker/docker-compose.yml down')

def start_finbench_dockers():
    if check_docker("docker_finbench_1") or check_docker("docker_tugraph_1"):
        stop_finbench_dockers()
    os.system('docker-compose -f ../docker/docker-compose.yml up -d')