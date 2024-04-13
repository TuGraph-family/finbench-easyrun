<template>
    <div class="performance">
        <div class="performance-title">性能测试结果</div>
        <div class="performance-list">
            <div>测试耗时：{{ result?.duration }} </div>
            <div>热身查询数：{{ result?.warmup }}</div>
            <div>总查询数：{{ result?.ops }} </div>
            <div>及时率：{{ result?.query_on_time }} </div>
            <div>性能吞吐：{{ result?.throughput }} </div>
        </div>
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