<template>
    <div class="logs">
        <div class="logs-title">
            系统日志：
        </div>
        <div class="logs-container" ref="logsContainer">
            <div v-for="(log, key) in logs" :key="key" class="log-entry">
                {{ key }}: {{ log }}
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { ref, computed, watch, nextTick } from 'vue'
import { useRunviewStore } from '@/stores/runview';
const runviewStore = useRunviewStore()
const logsContainer = ref<HTMLDivElement | null>(null);
let logs = computed(() => runviewStore.progressResult.logs)
watch(logs, async () => {
    await nextTick();
    if (logsContainer.value) {
        logsContainer.value.scrollTop = logsContainer.value.scrollHeight;
    }
});
</script>

<style scoped lang="less">
.logs {
    padding: 0 1.875rem 0.875rem 1.875rem;
    width: calc(100% - 3.75rem);
    height: 100%;

    .logs-title {
        display: flex;
        align-items: center;
        font-weight: 700;
        line-height: 40px;
        border-bottom: 1px dotted #424242;
        font-size: 1.125rem;
        margin-bottom: 0.625rem;
    }

    .logs-container {
        height: calc(100% - 60px);
        background-color: #333333;
        border-radius: 0.5rem;
        overflow-y: auto;

        >.log-entry {
            color: #FFD700;
            padding: 0.25rem 0.625rem;
        }
    }
}
</style>