# finbench-easyrun 

这是一个提供便捷、一站式地在TuGraph上运行LDBC FinBench的项目，包含相关Docker的构建，测试用脚本，使用说明等。

## 环境要求

- x86/arm CPU
- 已安装Docker和Docker compose环境，可运行Docker compose命令

## 使用说明

完整的测试流程除准备工作外，分为两个部分：
- 功能验证部分
- 性能验证部分

## 准备数据

数据生成是非必须的操作，可以通过`datasets/prepare_datasets.sh`直接下载预先生成好的数据。

使用生成好的数据集，参考“下载数据”章节，如果需要重新生成数据，参考“生成数据”章节

### 生成数据(非必须)

进入 `docker/deps/ldbc_finbench_datagen` 目录，

- 部署Spark：执行 `scripts/get-spark-to-home.sh` 下载预编译的Spark并解压，并将Spark的可执行文件的路径添加到环境变量里
- 构建项目：执行 `mvn clean package -DskipTests` 打包项目
- 执行`scripts/run_local.sh` 生成数据

注：修改`--scale-factor`参数可以调整生成数据集的目标规模

### 下载数据

开始测试前，需要准备好测试数据`SF1`和`SF10`，下载使用`prepare_datasets.sh`脚本，会在`datasets/`目录下下载测试数据，并进
行md5校验和数据的解压缩。

## 开始运行

### 白屏化页面运行

`backend`和`frontend`下面开发了一个简单的前后端供页面化操作Benchmark的执行

- 进入`backend`目录
- 静态链接静态资源：执行`ln -s ../frontend/dist ./static`
- 启动后端程序：`python3 backend.py`
- 打开终端提示的端口，根据页面进行操作

注：每次运行功能验证和性能验证前，需要重置整个系统，点击设置->重置系统

### 手动操作容器运行

#### 启动容器

使用如下命令，启动测试用容器。容器的配置详见`docker-compose.yml`
```
docker-compose up -d
```
容器启动后，会看到以下两个容器：`finbench-easyrun_tugraph_1`和`finbench-easyrun_finbench_1`

注：关于Docker构建，参考`TuGraphDB-Cent8-Dockerfile`和`FinBench-Cent8-Dockerfile`中的内容

#### 功能验证

数据正确下载后，开始进行功能验证。功能验证基于小规模SF1数据集，需要使用如下脚本

- 导入小规模数据：在`finbench-easyrun_tugraph_1`容器的`/root/scripts`目录下，执行`sf1_import.sh`
- 启动tugraph_server：在`finbench-easyrun_tugraph_1`容器的`/root/scripts`目录下，执行`sf1_start.sh`
- 安装Cpp插件：在`finbench-easyrun_finbench_1`容器的`/root/scripts`目录下，执行`load_procedure.sh`
- 进行功能验证：在`finbench-easyrun_finbench_1`容器的`/root/scripts`目录下，执行`sf1_validate.sh`

#### 性能验证

性能验证基于大规模SF10数据集，需要使用如下脚本

- 导入大规模数据：在`finbench-easyrun_tugraph_1`容器的`/root/scripts`目录下，执行`sf10_import.sh`
- 启动tugraph_server：在`finbench-easyrun_tugraph_1`容器的`/root/scripts`目录下，执行`sf10_start.sh`
- 安装Cpp插件：在`finbench-easyrun_finbench_1`容器的`/root/scripts`目录下，执行`load_procedure.sh`
- 进行性能测试：在`finbench-easyrun_finbench_1`容器的`/root/scripts`目录下，执行`sf10_benchmark.sh`

## FAQ

- Q: 报错`<jemalloc>: Unsupported system page size`问题
- A: Arm CPU兼容性问题，大部分Arm机器的PageSize并非4K，需要在该机器上重新编译TuGraph程序，参考`docker/TuGraphDB-Arm-Dockerfile`

