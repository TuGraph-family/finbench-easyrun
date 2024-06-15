<template>
    <div class="performance">
        <div class="performance-title">性能测试结果</div>
        <div class="performance-list">
            <el-tag>测试耗时：{{ (result?.total_duration / 1000000).toFixed(2) }} 秒 </el-tag>
            <!-- <div>热身查询数：{{ result?.warmup }}</div> -->
            <el-tag>总查询数：{{ Math.round(result?.total_count) }} 个 </el-tag>
            <!-- <div>及时率：{{ Math.round(result?.query_on_time || 0) }} </div> -->
            <el-tag>性能吞吐：{{ (result?.throughput).toFixed(2) }} QPS</el-tag>
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
        flex-direction: column;

        .el-tag {
            height: 3.125rem;
            margin-top: 0.625rem;
            font-size: 0.9rem;
        }
    }

}
</style>