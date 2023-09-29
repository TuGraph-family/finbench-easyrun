# finbench-easyrun

这是一个提供便捷、一站式地在TuGraph上运行LDBC FinBench的项目，包含相关Docker的构建，测试用脚本，使用说明等。

## 环境要求

- x86 CPU
- 已安装Docker和Docker compose环境，可运行Docker compose命令

## 使用说明

完整的测试流程除准备工作外，分为两个部分：
- 功能验证部分
- 性能验证部分

### 准备工作

#### 准备数据

开始测试前，需要准备好测试数据`SF1`和`SF10`，下载使用`prepare_datasets.sh`脚本，会在`datasets/`目录下下载测试数据，并进
行md5校验和数据的解压缩。

#### 启动容器

使用如下命令，启动测试用容器。容器的配置详见`docker-compose.yml`
```
docker-compose up -d
```
容器启动后，会看到以下两个容器：
- finbench-easyrun_tugraph_1
- finbench-easyrun_finbench_1

#### 安装Cpp插件

载`finbench-easyrun_finbench_1`容器的`/root/scripts`目录下，执行`load_procedure.sh`

至此，准备工作完毕

### 功能验证部分

数据正确下载后，开始进行功能验证。功能验证基于SF1数据集，需要使用如下脚本

- 在`finbench-easyrun_tugraph_1`容器的`/root/scripts`目录下，执行`sf1_import.sh`
- 在`finbench-easyrun_tugraph_1`容器的`/root/scripts`目录下，执行`sf1_start.sh`
- 在`finbench-easyrun_finbench_1`容器的`/root/scripts`目录下，执行`sf1_validate.sh`

### 性能验证部分

性能验证基于SF1数据集，需要使用如下脚本

- 在`finbench-easyrun_tugraph_1`容器的`/root/scripts`目录下，执行`sf10_import.sh`
- 在`finbench-easyrun_tugraph_1`容器的`/root/scripts`目录下，执行`sf10_start.sh`
- 在`finbench-easyrun_finbench_1`容器的`/root/scripts`目录下，执行`sf10_benchmark.sh`

## 关于Docker构建

参考`TuGraphDB-Cent8-Dockerfile`和`FinBench-Cent8-Dockerfile`中的内容

## 其他

注：选手可能提供新的tugraph-db的镜像。运行选手的镜像时，更新docker-compose.yml里面的内容