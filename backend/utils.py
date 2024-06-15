import os
import subprocess
import docker
import server

def check_docker(name):
    client = docker.from_env()
    return client.containers.list(filters={'name': name})

def stop_finbench_dockers():
    os.system('docker-compose -f ../docker-compose.yml down')

def start_finbench_dockers():
    if check_docker(server.FINBENCH_DOCKER) and check_docker(server.TUGRAPH_DOCKER):
        server.logger.warning('Docker containers already running.')
    else:
        os.system('docker-compose -f ../docker-compose.yml up -d')
    
def load_dataset(dataset):
    cmd = 'docker exec -it {} bash /root/scripts/{}_import.sh'.format(server.TUGRAPH_DOCKER, dataset)
    output = subprocess.run(cmd, capture_output=True, shell=True, text=True)
    return output.stdout.splitlines()

def start_tugraph(dataset):
    cmd_tmpl = 'docker exec -it {} bash /root/scripts/{}_start.sh'
    output = subprocess.run(cmd_tmpl.format(server.TUGRAPH_DOCKER, dataset), capture_output=True, shell=True, text=True)
    return output.stdout.splitlines()

def install_procedures():
    cmd_tmpl = 'docker exec -it {} bash /root/scripts/load_procedure.sh'
    output = subprocess.run(cmd_tmpl.format(server.FINBENCH_DOCKER), capture_output=True, shell=True, text=True)
    return output.stdout.splitlines()

def start_validate():
    cmd_tmpl = 'docker exec -it {} bash /root/scripts/sf1_validate.sh'
    p = subprocess.run(cmd_tmpl.format(server.FINBENCH_DOCKER), shell=True)
    return p

def start_benchmark(op_count, tcr):
    cmd_tmpl = 'docker exec -it {} bash /root/scripts/sf10_benchmark.sh {} {}'
    p = subprocess.run(cmd_tmpl.format(server.FINBENCH_DOCKER, op_count, tcr), shell=True)
    return p
  
def clean_log():
    logs = ["../scripts/validate_sf1.log", "../scripts/benchmark_sf10.log"]
    for log in logs:
        if os.path.exists(log):
            os.remove(log)