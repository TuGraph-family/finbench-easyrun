# validate on SF1 dataset

cd /root/ldbc/ldbc_finbench_transaction_impls/tugraph/

if ! [ -f ./target/tugraph-0.1.0-alpha.jar ]; then
    mvn clean package
fi

ln -s /root/datasets/validation_params.csv.sf1.20230605 ./validation_params.csv
cd data && ln -s /root/datasets/sf1 ./sf1 && cd ..
sed -i 's/172.21.189.228/tugraph/g'  validate_database.properties

bash run.sh validate_database.properties