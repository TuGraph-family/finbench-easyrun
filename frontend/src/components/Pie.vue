<template>
    <div class="pie">
        <div id="PieCanvas" ref="pieRef"></div>
    </div>
</template>
<script setup lang="ts">
import { ref, watch, computed, onMounted } from 'vue'
import { useRunviewStore } from '@/stores/runview'
import * as echarts from 'echarts'
const runviewStore = useRunviewStore()
const pieRef = ref<HTMLElement | null>(null)
let result = computed(() => runviewStore.result)
let pieData: Array<any> = []
let myChart: any = null
watch(result, (newResult) => {
    console.log(newResult)
    pieData = []
    newResult?.detail.forEach(item => {
        let obj = {
            name: item.name,
            value: item.count
        }
        pieData.push(obj)
    })
    myChart.setOption({
        legend: {
            type: 'scroll'
        },
        series: [{
            type: 'pie',
            data: pieData
        }]
    });
})
onMounted(() => {
    console.log(pieRef.value)
    myChart = echarts.init(pieRef.value, {}, {
        width: 500,
        height: 350,
    });
})

</script>

<style scoped lang="less">
.pie {
    width: 100%;
    text-align: center;
}
</style>