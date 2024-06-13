<template>
    <div class="modeinfo">
        <div class="modeinfo-title">模式配置</div>
        <div class="modeinfo-container">
            <div class="select-mode">
                <el-select v-model="mode">
                    <el-option value="validate" label="正确性验证">正确性验证</el-option>
                    <el-option value="benchmark" label="性能测试">性能测试</el-option>
                </el-select>
            </div>
            <template v-if="mode === 'benchmark'">
                <div class="tcr">
                    <el-input v-model="tcr" placeholder="压测参数">
                        <template #prepend>
                            <span class="input-prepend">压测参数：</span>
                        </template>
                    </el-input>
                </div>
                <div class="ops">
                    <el-input v-model="ops" placeholder="目标查询">
                        <template #prepend>
                            <span class="input-prepend">目标查询：</span>
                        </template>
                    </el-input>
                </div>
            </template>
            <div class="star-btn">
                <el-button type="warning" :disabled="runviewStore.systemStatus.uuid ? true : false"
                    @click="start">启动</el-button>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { ref, watch } from 'vue'
import type { Ref } from 'vue'
import { useRunviewStore } from '@/stores/runview';
const runviewStore = useRunviewStore()
const mode: Ref<'validate' | 'benchmark'> = ref('validate')
const tcr: Ref<number> = ref(0.01)
const ops: Ref<number> = ref(18000)
mode.value = runviewStore.modeInfo.mode
tcr.value = runviewStore.modeInfo.mode === 'benchmark' ? runviewStore.modeInfo.tcr : tcr.value
ops.value = runviewStore.modeInfo.mode === 'benchmark' ? runviewStore.modeInfo.ops : ops.value
watch([mode, tcr, ops], ([newMode, newTcr, newOps]) => {
    if (newMode === 'validate') {
        runviewStore.updateModeInfo({ mode: newMode })
    } else {
        runviewStore.updateModeInfo({ mode: newMode, tcr: newTcr, ops: newOps })
    }
})
async function start() {
    runviewStore.updateSystemStatus({ uuid: '' })
    clear()
    let res = await runviewStore.startTest(runviewStore.modeInfo)
    if (res.uuid) {
        runviewStore.updateSystemStatus({ uuid: res.uuid })
    }
}
function clear() {
    let initData = {
        "status": "",
        "duration": 0,
        "progress": 0,
        "logs": [],
        "num_lines": 0,
        "phase": '',
        runtime: 0,
        operations: 0,
        throughput: 0,
    }
    runviewStore.updateProgressResult(initData);
}
</script>

<style scoped lang="less">
.modeinfo {
    padding: 0 1.875rem 0.875rem 1.875rem;
    width: calc(100% - 3.75rem);

    .modeinfo-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-weight: 700;
        line-height: 40px;
        border-bottom: 1px dotted #424242;
        font-size: 1.125rem;

        .el-icon {
            cursor: pointer;
        }
    }

    .modeinfo-container {
        display: flex;
        padding: 0.625rem 0;

        >div {
            flex-grow: 1;
            margin-left: 0.625rem;
        }

        .select-mode {
            flex-grow: 0;
            width: 10rem;
            margin-left: 0;
        }

        .star-btn {
            width: 10rem;
            flex-grow: 0;

            .el-button {
                width: 100%;
            }
        }
    }
}
</style>