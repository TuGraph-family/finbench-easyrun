# validate on SF1 dataset

cd /root/ldbc/ldbc_finbench_transaction_impls/tugraph/

if ! [ -f ./target/tugraph-0.1.0-alpha.jar ]; then
    mvn clean package
fi

cd data && ln -s /root/datasets/sf10 ./sf10 && cd ..
sed -i 's/172.21.189.228/tugraph/g'  benchmark.properties

bash run.sh benchmark.properties