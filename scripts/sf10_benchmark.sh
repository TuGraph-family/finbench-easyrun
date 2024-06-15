# benchmarking on SF10 dataset
OP_COUNT=$1
TCR=$2

cd /root/ldbc/ldbc_finbench_transaction_impls/tugraph/

if ! [ -f ./target/tugraph-0.1.0-alpha.jar ]; then
    mvn clean package
fi
# soft link the data directory
if ! [ -d ./data/sf10 ]; then
cd data && ln -s /root/datasets/sf10 ./sf10 && cd ..
fi

sed -i 's/172.21.189.228/tugraph/g'  benchmark.properties

# update operations config
WARMUP_COUNT=$(($OP_COUNT/4))
sed -i "s/1800000/$OP_COUNT/g" benchmark.properties
sed -i "s/450000/$WARMUP_COUNT/g" benchmark.properties

# update tcr config
sed -i "s/0.1/$TCR/g" benchmark.properties

# run and record it to a log file in /root/script
bash run.sh benchmark.properties > /root/scripts/benchmark_sf10.log
cp /root/ldbc/ldbc_finbench_transaction_impls/tugraph/results/LDBC-FinBench-results.json /root/scripts/LDBC-FinBench-results.json