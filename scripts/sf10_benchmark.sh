# validate on SF1 dataset

cd /root/ldbc/ldbc_finbench_transaction_impls/tugraph/

if ! [ -f ./target/tugraph-0.1.0-alpha.jar ]; then
    mvn clean package
fi
# soft link the data directory
if ! [ -d ./data/sf10 ]; then
cd data && ln -s /root/datasets/sf10 ./sf10 && cd ..
fi

sed -i 's/172.21.189.228/tugraph/g'  benchmark.properties

# run and record it to a log file in /root/script
bash run.sh validate_database.properties > /root/scripts/benchmark_sf10.log