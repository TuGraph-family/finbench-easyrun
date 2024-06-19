# build tugraph-db docker image
docker build . -f TuGraphDB-Cent8-Dockerfile  \
    -t tugraph/finbench-easyrun-tugraphdb:cent8

docker build . -f TuGraphDB-Arm-Dockerfile \
    -t tugraph/finbench-easyrun-tugraphdb:arm-cent7

# build finbench docker image
docker build . -f FinBench-Cent8-Dockerfile  \
    -t tugraph/finbench-easyrun-finbench:cent8

docker build . -f FinBench-Arm-Dockerfile \
    -t tugraph/finbench-easyrun-finbench:arm-cent8
