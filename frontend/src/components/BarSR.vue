<template>
    <div class="bar-sr">
        <div class="bar-sr-title">简单读查询</div>
        <div class="bar-box">
            <div id="sr_1_min" ref="barSRRef_1_min"></div>
            <div id="sr_1_mean" ref="barSRRef_1_mean"></div>
            <div id="sr_1_max" ref="barSRRef_1_max"></div>
            <div id="sr_2" ref="barSRRef_2"></div>
        </div>

    </div>
</template>
<script setup lang="ts">
import { ref, watch, computed, onMounted } from 'vue'
import { useRunviewStore } from '@/stores/runview'
import * as echarts from 'echarts'
const runviewStore = useRunviewStore()
const barSRRef_1_min = ref<HTMLElement | null>(null)
const barSRRef_1_mean = ref<HTMLElement | null>(null)
const barSRRef_1_max = ref<HTMLElement | null>(null)
const barSRRef_2 = ref<HTMLElement | null>(null)
let result = computed(() => runviewStore.result)
let myChart_1_min: any = null
let myChart_1_mean: any = null
let myChart_1_max: any = null
let myChart_2: any = null
watch(result, () => {
    draw()
})
onMounted(() => {
    myChart_1_min = echarts.init(barSRRef_1_min.value, 'dark');
    myChart_1_mean = echarts.init(barSRRef_1_mean.value, 'dark');
    myChart_1_max = echarts.init(barSRRef_1_max.value, 'dark');
    myChart_2 = echarts.init(barSRRef_2.value, 'dark');
    if (result.value) {
        draw()
    }
})
function draw() {
    let legend_1_min: any = { data: [] }
    let legend_1_mean: any = { data: [] }
    let legend_1_max: any = { data: [] }
    let legend_2: any = { data: [] }
    let series_1_min: any = []
    let series_1_mean: any = []
    let series_1_max: any = []
    let series_2: any = []
    let unit: any = ''
    result.value.all_metrics.forEach(item => {
        if (item.name.startsWith('SimpleRead')) {
            unit = item.unit
            let obj_1_min = {
                name: item.name,
                type: 'bar',
                data: [item.run_time.min]
            }
            let obj_1_mean = {
                name: item.name,
                type: 'bar',
                data: [item.run_time.mean]
            }
            let obj_1_max = {
                name: item.name,
                type: 'bar',
                data: [item.run_time.max]
            }
            let obj_2 = {
                name: item.name,
                type: 'bar',
                data: [item.run_time['25th_percentile'], item.run_time['50th_percentile'], item.run_time['75th_percentile'], item.run_time['95th_percentile'], item.run_time['99th_percentile'], item.run_time['99.9th_percentile']]
            }
            legend_1_min.data.push(item.name)
            legend_1_mean.data.push(item.name)
            legend_1_max.data.push(item.name)
            legend_2.data.push(item.name)
            series_1_min.push(obj_1_min)
            series_1_mean.push(obj_1_mean)
            series_1_max.push(obj_1_max)
            series_2.push(obj_2)
        }
    })
    myChart_1_min.setOption({
        legend: legend_1_min,
        backgroundColor: '#333333',
        tooltip: {
            trigger: 'item',
            axisPointer: {
                type: 'shadow'
            }
        },
        xAxis: [
            {
                type: 'category',
                data: ["min"],
                axisPointer: {
                    type: 'shadow'
                }
            }
        ],
        yAxis: [
            {
                name: unit,
                type: 'value'
            }
        ],
        series: series_1_min
    });
    myChart_1_mean.setOption({
        legend: legend_1_mean,
        backgroundColor: '#333333',
        tooltip: {
            trigger: 'item',
            axisPointer: {
                type: 'shadow'
            }
        },
        xAxis: [
            {
                type: 'category',
                data: ["mean"],
                axisPointer: {
                    type: 'shadow'
                }
            }
        ],
        yAxis: [
            {
                name: unit,
                type: 'value'
            }
        ],
        series: series_1_mean
    });
    myChart_1_max.setOption({
        legend: legend_1_max,
        backgroundColor: '#333333',
        tooltip: {
            trigger: 'item',
            axisPointer: {
                type: 'shadow'
            }
        },
        xAxis: [
            {
                type: 'category',
                data: ["max"],
                axisPointer: {
                    type: 'shadow'
                }
            }
        ],
        yAxis: [
            {
                name: unit,
                type: 'value'
            }
        ],
        series: series_1_max
    });
    myChart_2.setOption({
        legend: legend_2,
        backgroundColor: '#333333',
        tooltip: {
            trigger: 'item',
            axisPointer: {
                type: 'shadow'
            }
        },
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
                name: unit,
                type: 'value'
            }
        ],
        series: series_2
    });
}
</script>

<style scoped lang="less">
.bar-sr {

    // width: 100%;
    // height: 600px;
    padding: 3px 10px;

    .bar-sr-title {
        font-weight: bolder;
        font-size: 18px;
    }

    #sr_1_min {
        width: 50%;
        height: 300px;

    }

    #sr_1_mean {
        width: 50%;
        height: 300px;

    }

    #sr_1_max {
        width: 50%;
        height: 300px;

    }

    #sr_2 {
        width: 50%;
        height: 300px;
    }

    .bar-box {
        width: 100%;
        height: 600px;
        display: flex;
        flex-wrap: wrap;
    }
}
</style>