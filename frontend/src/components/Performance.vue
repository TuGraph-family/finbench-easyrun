<template>
    <div class="performance">
        <div>测试耗时：{{ result?.duration }} </div>
        <div>热身查询数：{{ result?.warmup }}</div>
        <div>总查询数：{{ result?.ops }} </div>
        <div>及时率：{{ result?.query_on_time }} </div>
        <div>性能吞吐：{{ result?.throughput }} </div>
    </div>
</template>
<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import { useRunviewStore } from '@/stores/runview';


const runviewStore = useRunviewStore()
let result = computed(() => runviewStore.result)


</script>

<style scoped lang="less">
.performance {
    height: 100%;
    width: 100%;
}
</style>