<template>
    <div class="finbench-result">
        <div class="performance-result">
            <div style="width: 18.75rem;">
                <Performance />
            </div>
            <div style="flex-grow: 1;height: 100%;">
                <Pie />
            </div>
        </div>
        <div class="performance-CR">
            <BarCR />
        </div>
        <div class="performance-SR">
            <BarSR />
        </div>
        <div class="performance-W">
            <BarW />
        </div>
        <div class="performance-RW">
            <BarRW />
        </div>
    </div>
</template>
<script setup lang="ts">
import { watch, computed } from 'vue'
import { useRunviewStore } from '@/stores/runview';
import Performance from './Performance.vue'
// Abstract optimization after the Echarts component code.
import Pie from './Pie.vue'
import BarCR from './BarCR.vue'
import BarSR from './BarSR.vue'
import BarW from './BarW.vue'
import BarRW from './BarRW.vue'
const runviewStore = useRunviewStore()
let result = computed(() => runviewStore.result)
watch(result, () => {
    console.log(result)
})



</script>

<style scoped lang="less">
.finbench-result {

    .performance-result,
    .performance-CR,
    .performance-SR,
    .performance-W,
    .performance-RW {
        border: 5px solid #ddd;
        border-radius: 8px;
        margin-top: 20px;
        background-color: #333333;
    }

    .performance-result {
        display: flex;

    }
}
</style>