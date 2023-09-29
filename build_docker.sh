# build tugraph-db docker image
docker build . -f TuGraphDB-Cent8-Dockerfile  \
    -t tugraph/tugraph-bdci-tugraphdb:cent8

# build finbench docker image
docker build . -f FinBench-Cent8-Dockerfile  \
    -t tugraph/tugraph-bdci-finbench:cent8
