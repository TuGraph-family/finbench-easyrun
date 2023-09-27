OSS_PREFIX=https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/finbench/v0.1.0

function download_and_check() {
    if [ -f datasets/$1 ]; then
        echo "$1 exists, skip downloading"
        return
    fi
    wget -q ${OSS_PREFIX}/$1 -O datasets/$1
    wget -q ${OSS_PREFIX}/$1.md5sum -O datasets/$1.md5sum
    cd datasets/ && md5sum -c $1.md5sum && cd ..
}

# set -x

download_and_check sf1_read_params.zip
download_and_check sf10_read_params.zip
download_and_check sf1.tar.gz
download_and_check sf10.tar.gz
download_and_check validation_params.csv.sf1.20230605