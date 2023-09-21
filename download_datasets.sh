set -x

wget -q https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/finbench/v0.1.0/sf1.tar.gz && tar zxf sf1.tar.gz && ls sf1
wget -q https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/finbench/v0.1.0/sf10.tar.gz && tar zxf sf10.tar.gz && ls sf10
wget -q https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/finbench/v0.1.0/sf1_read_params.zip && unzip sf1_read_params.zip && ls sf1_read_params
wget -q https://tugraph-web.oss-cn-beijing.aliyuncs.com/tugraph/datasets/finbench/v0.1.0/sf10_read_params.zip && sf10_read_params.zip && unzip sf10_read_params.zip && ls sf10_read_params