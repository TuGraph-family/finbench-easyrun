<template>
    <div class="progress">
        <div>
            <div class="progress-title">
                <span>
                    执行状态：
                </span>
                <span>
                    {{ status }}
                </span>
                <span style="margin-left:0.9375rem ;">
                    当前步骤：
                </span>
                <span>
                    {{ phase }}
                </span>
                <el-tag style="margin-left: 0.9375rem;" size="large"
                    v-if="status == 'Completed' && mode == 'validate'">验证通过</el-tag>
            </div>
            <div>
                <el-progress :percentage="progress" />
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { computed, onUnmounted, watch } from 'vue'
import { useRunviewStore } from '@/stores/runview';
const runviewStore = useRunviewStore()
let uuid = runviewStore.systemStatus.uuid
let progress = computed(() => runviewStore.progressResult.progress)
let phase = computed(() => runviewStore.progressResult.phase)
let status = computed(() => runviewStore.progressResult.status)
let isReseting = computed(() => runviewStore.isReseting)
let mode = computed(() => runviewStore.modeInfo.mode)
let timer: any = 0
watch(isReseting, () => {
    clearInterval(timer);
})
watch(status, () => {
    if (status.value === 'Failed') {
        clearInterval(timer)
    }
})
async function getProgress() {
    timer = setInterval(async () => {
        let res: any;
        if (uuid) {
            res = await runviewStore.getProgress(uuid);
            runviewStore.updateProgressResult(res);
            if (res.status === 'Completed') {
                clearInterval(timer);
            }
        }
    }, 1000);
}
onUnmounted(() => {
    clearInterval(timer);
});
if (runviewStore.progressResult.status !== 'Completed' && runviewStore.progressResult.status !== 'Failed' && uuid) {
    getProgress()
}

</script>

<style scoped lang="less">
.progress {
    padding: 0 1.875rem 0.875rem 1.875rem;
    width: calc(100% - 3.75rem);

    .progress-title {
        display: flex;
        align-items: center;
        font-weight: 700;
        line-height: 40px;
        border-bottom: 1px dotted #424242;
        font-size: 1.125rem;
        margin-bottom: 0.625rem;
    }
}
</style>