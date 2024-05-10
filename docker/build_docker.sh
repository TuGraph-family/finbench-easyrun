# build tugraph-db docker image
docker build . -f TuGraphDB-Cent8-Dockerfile  \
    -t tugraph/tugraph-bdci-tugraphdb:cent8

docker build . -f TuGraphDB-Arm-Dockerfile \
    -t tugraph/tugraph-bdci-tugraphdb:arm

# build finbench docker image
docker build . -f FinBench-Cent8-Dockerfile  \
    -t tugraph/tugraph-bdci-finbench:cent8

docker build . -f FinBench-Arm-Dockerfile \
    -t tugraph/tugraph-bdci-finbench:arm
