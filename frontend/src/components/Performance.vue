<template>
    <div class="performance">
        <div class="performance-title">性能测试结果</div>
        <div class="performance-list">
            <div>测试耗时：{{ (result?.total_duration / 1000000).toFixed(2) }} 秒 </div>
            <!-- <div>热身查询数：{{ result?.warmup }}</div> -->
            <div>总查询数：{{ Math.round(result?.total_count) }} 个 </div>
            <div>及时率：{{ Math.round(result?.query_on_time || 0) }} </div>
            <div>性能吞吐：{{ (result?.throughput).toFixed(2) }} </div>
        </div>
    </div>

</template>
<script setup lang="ts">
import { computed } from 'vue'
import { useRunviewStore } from '@/stores/runview';


const runviewStore = useRunviewStore()
let result = computed(() => runviewStore.result)


</script>

<style scoped lang="less">
.performance {
    height: 60px;
    padding: 3px 10px;

    .performance-title {
        font-weight: bolder;
        font-size: 18px;

    }

    .performance-list {
        display: flex;

        >div {
            flex: 1;
            line-height: 50px;
        }
    }

}
</style>