<template>
    <div class="finbech-progress">
        <div class="progress-result">
            <div>
                <div>测试结果</div>
                <div v-if="proStatus === 'running'">
                    执行中
                </div>
                <div v-else>
                    待执行
                </div>
            </div>
            <template v-if="runviewStore.modeInfo.mode === 'benchmark'">
                <div>
                    <div>
                        测试时间
                    </div>
                    <div>
                        {{ duration || 0 }}秒
                    </div>
                </div>
                <div>
                    <div>测试进度</div>
                    <div>
                        <el-progress :percentage="progress" />
                    </div>
                </div>
            </template>
        </div>
        <div class="btn-run">
            <el-button type="danger"
                :disabled="runviewStore.systemStatus.status !== 'start' || runviewStore.progressResult.status === 'running'"
                circle @click="run">
                启动
            </el-button>
        </div>
    </div>
</template>
<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRunviewStore } from '@/stores/runview';
const runviewStore = useRunviewStore()
let uuid = runviewStore.systemStatus.uuid
let status = computed(() => runviewStore.systemStatus.status)
let proStatus = computed(() => runviewStore.progressResult.status)
let duration = computed(() => runviewStore.progressResult.duration)
let progress = computed(() => runviewStore.progressResult.progress)
async function run() {
    console.log(runviewStore.progressResult.status)
    if (status.value === 'start') {
        let res = await runviewStore.getProgress(uuid)
        runviewStore.updateProgressResult(res)
        // 伪逻辑--start
        let n = 2

        let timer = setInterval(async () => {
            runviewStore.updateProgressResult({ status: 'running', duration: 1 * n, progress: 10 * n })
            n++
            if (n > 10) {
                clearInterval(timer)
                let res = await runviewStore.getResult(uuid)
                console.log(123131312)
                runviewStore.updateResult(res)
                runviewStore.updateProgressResult({ status: 'finished', duration: 1 * n, progress: 100 })
            }
        }, 1000)
        // 伪逻辑--end
    }
}
</script>

<style scoped lang="less">
.finbech-progress {
    display: flex;
    padding: 10px;

    .progress-result {
        flex-grow: 1;
        display: flex;

        >div {
            margin-right: 30px;

            >div {
                line-height: 40px;

                .el-progress {
                    margin-top: 13px;
                    width: 200px;
                }
            }
        }
    }

    .btn-run {
        flex-grow: 0;
    }

    .el-button {
        width: 80px;
        height: 80px;
        font-size: 30px;
    }
}
</style>