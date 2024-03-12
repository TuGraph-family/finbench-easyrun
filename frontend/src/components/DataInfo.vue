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
                <el-button>加载数据</el-button>
            </div>
            <div class="btn-start-system">
                <el-button>启动系统</el-button>
            </div>
        </div>


    </div>
</template>
<script setup lang="ts">
import { ref } from 'vue'
import { useRunviewStore } from '@/stores/runview';
const data = ref('')
const runviewStore = useRunviewStore()

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
        row-gap: 10px;
        padding: 10px;
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