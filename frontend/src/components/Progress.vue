<template>
    <div class="progress">
        <div>
            <div class="progress-title">
                <span>
                    执行进度：
                </span>
                <span>
                    {{ status }}
                </span>
            </div>
            <div>
                <el-progress :percentage="progress" />
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { computed, onUnmounted } from 'vue'
import { useRunviewStore } from '@/stores/runview';
const runviewStore = useRunviewStore()
let uuid = runviewStore.systemStatus.uuid
let progress = computed(() => runviewStore.progressResult.progress)
let status = computed(() => runviewStore.progressResult.status)
let timer: any = 0
async function getProgress() {

    let startTime = Date.now()
    timer = setInterval(async () => {
        let res: any;
        if (uuid !== 'test_uuid') {
            res = await runviewStore.getProgress(uuid);
        } else {
            res = await runviewStore.getTestProgress(uuid, startTime);
        }
        runviewStore.updateProgressResult(res);
        if (res.status === 'completed') {
            clearInterval(timer);
        }
    }, 1000);
}
onUnmounted(() => {
    clearInterval(timer);
});
if (runviewStore.progressResult.status !== 'completed') {
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