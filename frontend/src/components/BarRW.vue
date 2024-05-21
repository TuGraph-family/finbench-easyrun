<template>
    <div class="barRW">
        <div class="barRW-title">混合查询</div>
        <div id="rw_1" ref="barRWRef_1"></div>
        <div id="rw_2" ref="barRWRef_2"></div>
    </div>
</template>
<script setup lang="ts">
import { ref, watch, computed, onMounted } from 'vue'
import { useRunviewStore } from '@/stores/runview'
import * as echarts from 'echarts'
const runviewStore = useRunviewStore()
const barRWRef_1 = ref<HTMLElement | null>(null)
const barRWRef_2 = ref<HTMLElement | null>(null)
let result = computed(() => runviewStore.result)
let myChart_1: any = null
let myChart_2: any = null
watch(result, (newResult) => {
    draw()
})
onMounted(() => {
    myChart_1 = echarts.init(barRWRef_1.value,'dark');
    myChart_2 = echarts.init(barRWRef_2.value,'dark');
    if (result.value) {
        draw()
    }
})
function draw() {
    let legend_1: any = { data: [] }
    let legend_2: any = { data: [] }
    let series_1: any = []
    let series_2: any = []
    result.value.detail.forEach(item => {
        if (item.name.startsWith('RW')) {
            let obj_1 = {
                name: item.name,
                type: 'bar',
                data: [item.run_time.min, item.run_time.mean, item.run_time.max]
            }
            let obj_2 = {
                name: item.name,
                type: 'bar',
                data: [item.run_time['25th_percentile'], item.run_time['50th_percentile'], item.run_time['75th_percentile'], item.run_time['95th_percentile'], item.run_time['99th_percentile'], item.run_time['99.9th_percentile']]
            }
            legend_1.data.push(item.name)
            legend_2.data.push(item.name)
            series_1.push(obj_1)
            series_2.push(obj_2)
        }
    })
    myChart_1.setOption({
        legend: legend_1,
        xAxis: [
            {
                type: 'category',
                data: ["min", "mean", "max"],
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
        series: series_1
    });
    myChart_2.setOption({
        legend: legend_2,
        xAxis: [
            {
                type: 'category',
                data: ['25th_percentile', '50th_percentile', '75th_percentile', '95th_percentile', '99th_percentile', '99.9th_percentile'],
                axisPointer: {
                    type: 'shadow'
                },
                axisLabel: {
                    interval: 0
                }
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: series_2
    });
}
</script>

<style scoped lang="less">
.barRW {

    // width: 100%;
    // height: 600px;
    padding: 3px 10px;

    .barRW-title {
        font-weight: bolder;
        font-size: 18px;
    }

    #rw_1 {
        width: 100%;
        height: 300px;
    }

    #rw_2 {
        width: 100%;
        height: 300px;
    }
}
</style>