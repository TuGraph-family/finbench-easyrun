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
    if (result.value) {
        draw()
    }
})
function draw() {
    pieData = []
    let n = 0.1
    let total_count = result.value.total_count
    result.value.all_metrics.forEach(item => {
        let obj: any = {}
        if (item.count > total_count * n) {
            obj = {
                name: item.name,
                value: item.count
            }
            pieData.push(obj)
        } else {
            let current_ohter = pieData.find(item => item.name == 'other')
            if (current_ohter) {
                let current_count = current_ohter ? current_ohter.value : 0
                current_ohter = {
                    name: 'other',
                    value: current_count + item.count
                }
            } else {
                obj = {
                    name: 'other',
                    value: item.count
                }
                pieData.push(obj)
            }
        }
    })
    myChart.setOption({
        backgroundColor: '#333333',
        legend: {
            type: 'scroll'
        },
        tooltip: {
            trigger: 'item'
        },
        series: [{
            type: 'pie',
            data: pieData.reverse()
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