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
watch(result, () => {
    draw()
})
onMounted(() => {
    myChart = echarts.init(pieRef.value, 'dark');
    console.log(result.value)
    if (result.value) {

        draw()
    }
})
function draw() {
    pieData = []
    result.value.detail.forEach(item => {
        let obj = {
            name: item.name,
            value: item.count
        }
        pieData.push(obj)
    })
    myChart.setOption({
        backgroundColor: '#333333',
        legend: {
            type: 'scroll'
        },
        series: [{
            type: 'pie',
            data: pieData
        }]
    });
}

</script>

<style scoped lang="less">
.pie {
    width: clac(100% - 20px);
    height: 400px;
    text-align: center;
    padding: 10px;

    >#PieCanvas {
        width: 100%;
        height: 100%;
    }
}
</style>