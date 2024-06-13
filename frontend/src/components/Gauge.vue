<template>
    <div class="bar-cr">
        <div id="gauge" ref="Gauge"></div>
    </div>
</template>
<script setup lang="ts">
import { ref, watch, computed, onMounted } from 'vue'
import { useRunviewStore } from '@/stores/runview'
import * as echarts from 'echarts'
const runviewStore = useRunviewStore()
const Gauge = ref<HTMLElement | null>(null)
let result = computed(() => runviewStore.result)
let myChart_1: any = null
let myChart_2: any = null
watch(result, () => {
    draw()
})
onMounted(() => {
    myChart_1 = echarts.init(Gauge.value, 'dark');
    if (result.value) {
        draw()
    }
})
function draw() {
    myChart_1.setOption({
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
        series: {}
    });

}
</script>

<style scoped lang="less">
.bar-cr {

    // width: 100%;
    // height: 600px;
    padding: 3px 10px;

    .bar-cr-title {
        font-weight: bolder;
        font-size: 18px;
    }

    #cr_1 {
        width: 100%;
        height: 300px;
    }

    #cr_2 {
        width: 100%;
        height: 300px;
    }
}
</style>