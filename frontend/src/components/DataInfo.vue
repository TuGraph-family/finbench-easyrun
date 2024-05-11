<template>
    <div class="finbech-datainfo">
        <div class="finbech-datainfo-title">数据配置</div>
        <div class="finbech-datainfo-container">
            <div class="finbech-datainfo-img"></div>
            <div class="finbech-datainfo-name">测试数据</div>
            <div>
                <el-select v-model="data" placeholder="请选择数据">
                    <el-option v-for="item in runviewStore.dataList" :key="item" :label="item" :value="item">
                    </el-option>
                </el-select>
            </div>
            <div class="btn-load-data">
                <el-button v-if="runviewStore.dataLoad === 'waiting'" @click="loadData" :disabled="runviewStore.dataLoad !=='waiting'">
                    <span>请先加载数据</span>
                </el-button>
                <el-button v-if="runviewStore.dataLoad === 'loading'" loading disabled>
                    <span>加载数据中</span>
                </el-button>
                <el-button v-if="runviewStore.dataLoad === 'finished'" disabled>
                    <span>加载数据完成</span>
                </el-button>
            </div>
            <div class="btn-start-system">
                <el-button v-if="runviewStore.systemStatus.status === 'stop'" :disabled="runviewStore.dataLoad !== 'finished'"
                    @click="startSut">启动系统</el-button>
                <el-button v-else :disabled="runviewStore.systemStatus.status === 'start'"
                    @click="startSut">系统已启动</el-button>
            </div>
        </div>
    </div>
</template>
<script setup lang="ts">
import { ref, watch } from 'vue'
import { useRunviewStore } from '@/stores/runview';
const runviewStore = useRunviewStore()
const data = ref('')
data.value = runviewStore.dataInfo.data
// 获取可用数据集
runviewStore.getListDataset()
// 监听 data 的变化，并更新 Pinia store 中的 dataInfo.data
watch(data, (newValue) => {
    runviewStore.updateDataInfo({ data: newValue })
    runviewStore.updateLoadData('waiting')
    runviewStore.updateSystemStatus({ uuid: '', status: 'stop' })
    runviewStore.updateProgressResult({ status: '', duration: 0, progress: 0 })
})

async function loadData() {
    runviewStore.updateLoadData('loading')
    let res: string = await runviewStore.runLoadDatase()
    if (res === 'ok') {
        runviewStore.updateLoadData('finished')
    }

}

async function startSut() {
    let res = await runviewStore.startSut()
    runviewStore.updateSystemStatus({ uuid: res.uuid, status: 'start' })
}
</script>

<style scoped lang="less">
.finbech-datainfo {
    width: 100%;

    &-title {
        font-weight: bolder;
        font-size: 18px;
        padding: 3px 10px;
        border-bottom: 1px solid #ddd;
    }

    &-container {
        display: grid;
        grid-template-columns: 100px auto;
        column-gap: 20px;
        padding: 10px;
        row-gap: 10px;
    }

    &-img {
        margin: 0 10px 10px 0;
        width: 100px;
        height: 100px;
        background-image: url('../assets/data.png');
        background-size: contain;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .btn-load-data {
        grid-column-start: 1;
        grid-column-end: 3;
    }

    .btn-start-system {
        grid-column-start: 1;
        grid-column-end: 3;
    }

    .el-button {
        width: 100%;
    }
}
</style>