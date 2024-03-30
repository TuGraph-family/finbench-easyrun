<template>
    <div class="bar-left">
        <div ref="barLeftRef"></div>
    </div>
</template>
<script setup lang="ts">
import { ref, watch, computed, onMounted } from 'vue'
import { useRunviewStore } from '@/stores/runview'
import * as echarts from 'echarts'
const runviewStore = useRunviewStore()
const barLeftRef = ref<HTMLElement | null>(null)
let result = computed(() => runviewStore.result)
let pieData: Array<any> = []
let myChart: any = null
watch(result, (newResult) => {
    console.log(newResult)
    let legend: any = { data: [] }
    let series: any = []
    newResult?.detail.forEach(item => {
        let obj = {
            name: item.name,
            value: item.count
        }
        legend.data.push(obj)
    })
    myChart.setOption({
        legend: legend,
        xAxis: [
            {
                type: 'category',
                data: ["mean", "min", "max"],
                axisPointer: {
                    type: 'shadow'
                }
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: series
    });
})
onMounted(() => {
    myChart = echarts.init(barLeftRef.value, {}, {
        width: 500,
        height: 350,
    });
})

</script>

<style scoped lang="less">
.bar-left {
    width: 100%;
    text-align: center;
}
</style>