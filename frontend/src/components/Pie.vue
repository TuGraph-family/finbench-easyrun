<template>
    <div class="pie">
        <el-tabs v-model="activeName" type="card" class="demo-tabs" stretch>
            <el-tab-pane label="复杂读查询" name="ComplexRead">
                <div id="PieCanvas1" ref="pieRef1"></div>
            </el-tab-pane>
            <el-tab-pane label="简单读查询" name="SimpleRead">
                <div id="PieCanvas2" ref="pieRef2"></div>
            </el-tab-pane>
            <el-tab-pane label="写查询" name="Write">
                <div id="PieCanvas3" ref="pieRef3"></div>
            </el-tab-pane>
            <el-tab-pane label="混合查询" name="ReadWrite">
                <div id="PieCanvas4" ref="pieRef4"></div>
            </el-tab-pane>
        </el-tabs>

    </div>
</template>
<script setup lang="ts">
import { ref, watch, computed, onMounted, nextTick } from 'vue'
import { useRunviewStore } from '@/stores/runview'
import * as echarts from 'echarts'
const runviewStore = useRunviewStore()
const pieRef1 = ref<HTMLElement | null>(null)
const pieRef2 = ref<HTMLElement | null>(null)
const pieRef3 = ref<HTMLElement | null>(null)
const pieRef4 = ref<HTMLElement | null>(null)
let result = computed(() => runviewStore.result)
let pieData1: Array<any> = []
let myChart1: any = null
let pieData2: Array<any> = []
let myChart2: any = null
let pieData3: Array<any> = []
let myChart3: any = null
let pieData4: Array<any> = []
let myChart4: any = null
let activeName = ref('ComplexRead')
watch(result, () => {
    draw()
})
onMounted(async () => {
    await nextTick()
    let height = pieRef1.value?.clientHeight
    let width = pieRef1.value?.clientWidth
    myChart1 = echarts.init(pieRef1.value, 'dark', { width, height });
    myChart2 = echarts.init(pieRef2.value, 'dark', { width, height });
    myChart3 = echarts.init(pieRef3.value, 'dark', { width, height });
    myChart4 = echarts.init(pieRef4.value, 'dark', { width, height });
    if (result.value) {
        draw()
    }
})
function draw() {
    pieData1 = []
    pieData2 = []
    pieData3 = []
    pieData4 = []
    let base = {
        backgroundColor: '#333333',
        legend: {
            type: 'scroll'
        },
        tooltip: {
            trigger: 'item'
        },
    }
    result.value.all_metrics.forEach(item => {
        if (item.name.startsWith('ComplexRead')) {
            let obj: any = {}
            obj = {
                name: item.name,
                value: item.count
            }
            pieData1.push(obj)
        }
        if (item.name.startsWith('SimpleRead')) {
            let obj: any = {}
            obj = {
                name: item.name,
                value: item.count
            }
            pieData2.push(obj)
        }
        if (item.name.startsWith('Write')) {
            let obj: any = {}
            obj = {
                name: item.name,
                value: item.count
            }
            pieData3.push(obj)
        }
        if (item.name.startsWith('ReadWrite')) {
            let obj: any = {}
            obj = {
                name: item.name,
                value: item.count
            }
            pieData4.push(obj)
        }
    })
    myChart1.setOption({
        ...base,
        series: [{
            type: 'pie',
            data: pieData1
        }]
    });
    myChart2.setOption({
        ...base,
        series: [{
            type: 'pie',
            data: pieData2
        }]
    });
    myChart3.setOption({
        ...base,
        series: [{
            type: 'pie',
            data: pieData3
        }]
    });
    myChart4.setOption({
        ...base,
        series: [{
            type: 'pie',
            data: pieData4
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



    .el-tabs {
        width: 100%;
        height: 100%;

        :deep(.el-tabs__content) {
            width: 100%;
            height: calc(100% - 2.825rem);

            >div {
                width: 100%;
                height: 100%;

                >#PieCanvas1 {
                    width: 100%;
                    height: 100%;
                }

                >#PieCanvas2 {
                    width: 100%;
                    height: 100%;
                }
            }
        }
    }
}
</style>