<template>
    <div class="gauge">
        <div
            style="line-height: 40px; margin-bottom: 10px; display: flex; justify-content: space-between;align-items: center;">
            <span>
                运行时长：{{ runtime }}
            </span>
            <span>
                OP数：{{ operations }}
            </span>
        </div>
        <div id="gauge" ref="Gauge"></div>
    </div>
</template>
<script setup lang="ts">
import { ref, watch, computed, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { useRunviewStore } from '@/stores/runview'
import * as echarts from 'echarts'
const runviewStore = useRunviewStore()
const Gauge = ref<HTMLElement | null>(null)
let myChart_1: any = null
let throughput = computed(() => runviewStore.progressResult.throughput)
let runtime = computed(() => runviewStore.progressResult.runtime)
let operations = computed(() => runviewStore.progressResult.operations)
let default_max = ref(100)
let max = ref(0)
let resizeObserver: ResizeObserver | null = null
watch(throughput, () => {
    if (throughput.value > max.value) {
        max.value = throughput.value
    }
    draw()
})
onMounted(async () => {
    await nextTick()
    let width = Gauge.value?.clientWidth
    let height = Gauge.value?.clientHeight
    console.log(width, height)
    myChart_1 = echarts.init(Gauge.value, 'dark', { width: width, height: height });
    draw()
    resizeObserver = new ResizeObserver(() => {
        resizeChart()
    })
    if (Gauge.value) {
        resizeObserver.observe(Gauge.value)
    }

    // 添加窗口大小变化的监听器作为后备
    window.addEventListener('resize', resizeChart)
    window.addEventListener('resize', resizeChart)
})
function draw() {
    let option = {
        backgroundColor: '#333333',
        tooltip: {
            formatter: '{a} <br/>{b} : {c}%'
        },
        series: [
            {
                name: 'Pressure',
                type: 'gauge',
                progress: {
                    show: true
                },
                detail: {
                    valueAnimation: true,
                    formatter: '{value}'
                },
                min: 0,
                max: max.value || default_max.value,
                data: [
                    {
                        value: throughput.value,
                        name: 'THROUGHPUT'
                    }
                ]
            }
        ]
    };
    myChart_1.setOption(option);
}
function resizeChart() {
    if (myChart_1) {
        let width = Gauge.value?.clientWidth
        let height = Gauge.value?.clientHeight
        myChart_1.resize({ width, height })
    }
}
onBeforeUnmount(() => {
    // 移除窗口大小变化的监听器
    window.removeEventListener('resize', resizeChart)
    if (myChart_1) {
        myChart_1.dispose()
    }
})
</script>

<style scoped lang="less">
.gauge {
    width: 100%;
    width: 100%;
    height: 100%;

    #gauge {
        border-radius: 8px;
        width: 100%;
        height: calc(100% - 45px);
        overflow: hidden;

    }
}
</style>