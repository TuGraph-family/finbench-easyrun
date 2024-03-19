<template>
    <div class="finbench-result">
        <div class="result">
            <el-tabs :stretch="true">
                <el-tab-pane label="性能测试结果">
                    <div class="res-1">
                        <div class="left">
                            <div>测试耗时：{{ result?.duration }} </div>
                            <div>热身查询数：{{ result?.warmup }}</div>
                            <div>总查询数：{{ result?.ops }} </div>
                            <div>及时率：{{ result?.query_on_time }} </div>
                            <div>性能吞吐：{{ result?.throughput }} </div>
                        </div>
                        <div class="right" ref="">

                        </div>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="热点分析">
                    <div class="res-2">
                        <el-tabs tab-position="left">
                            <el-tab-pane label="复杂读查询">复杂读查询</el-tab-pane>
                            <el-tab-pane label="简单读查询">简单读查询</el-tab-pane>
                            <el-tab-pane label="写查询">写查询</el-tab-pane>
                            <el-tab-pane label="混合写查询">混合写查询</el-tab-pane>
                        </el-tabs>
                    </div>
                </el-tab-pane>
            </el-tabs>
        </div>
    </div>

</template>
<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import { useRunviewStore } from '@/stores/runview';
import * as echarts from 'echarts';
var myChart = echarts.init(document.getElementById('main'));
const runviewStore = useRunviewStore()
let result = computed(() => runviewStore.result)
watch(result, () => {
    console.log(result)
})

</script>

<style scoped lang="less">
.finbench-result {
    height: 100%;

    .result {
        width: 100%;
        height: 100%;
    }

    .no-result {
        text-align: center;
        padding-top: 150px;
    }


    .el-tabs__content {
        height: 100%;
    }

    .res-1 {
        display: flex;

        .left {
            width: 200px;
            margin-right: 20px;
        }
    }

    .res-2 {
        padding: 0 15px;
        height: 100%;

        .el-tabs {
            height: 100%;
            border-radius: 5px;
        }

    }

}
</style>