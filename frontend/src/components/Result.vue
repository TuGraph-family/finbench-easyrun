<template>
    <div class="finbench-result">
        <div class="result">
            <el-tabs :stretch="true">
                <el-tab-pane label="性能测试结果">
                    <div class="res-1">
                        <div class="left">
                            <Performance />
                        </div>
                        <div class="right">
                            <Pie />
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
import Performance from './Performance.vue'
import Pie from './Pie.vue'
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

            .right {
                flex-grow: 1;

                .pie {
                    width: 100%;
                    height: 100%;
                }
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
}
</style>