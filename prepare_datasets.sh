OSS_PREFIX=https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/bdci

function download_and_check() {
    if [ -f datasets/$1 ]; then
        echo "$1 exists, skip downloading"
        cd datasets/ && md5sum -c $1.md5sum && cd ..
        return
    fi
    wget -q ${OSS_PREFIX}/$1 -O datasets/$1
    wget -q ${OSS_PREFIX}/$1.md5sum -O datasets/$1.md5sum
    cd datasets/ && md5sum -c $1.md5sum && cd ..
}

set -x

download_and_check sf1_withparams.tar.gz
download_and_check sf10_withparams.tar.gz
download_and_check validation_params.csv.sf1.20230605

# extract
cd datasets/
tar zxf sf1_withparams.tar.gz
tar zxf sf10_withparams.tar.gz