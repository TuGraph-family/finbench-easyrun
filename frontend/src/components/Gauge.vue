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
import { ref, watch, computed, onMounted } from 'vue'
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
watch(throughput, () => {
    if (throughput.value > max.value) {
        max.value = throughput.value
    }
    draw()
})
onMounted(() => {
    let width = Gauge.value?.clientWidth
    let height = Gauge.value?.clientHeight
    myChart_1 = echarts.init(Gauge.value, 'dark', { width: width, height: height });
    draw()
})
function draw() {
    let option = {
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
                        name: 'SCORE'
                    }
                ]
            }
        ]
    };
    myChart_1.setOption(option);
}
</script>

<style scoped lang="less">
.gauge {
    width: 100%;
    width: 100%;
    height: 100%;

    #gauge {
        width: 100%;
        height: 100%;

    }
}
</style>