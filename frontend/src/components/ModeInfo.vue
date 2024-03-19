<template>
    <div class="finbech-modeinfo">
        <div class="finbech-modeinfo-title">模式配置</div>
        <div class="finbech-modeinfo-container">
            <div class="finbech-modeinfo-img"></div>
            <div>测试模式</div>
            <div>
                <el-radio v-model="mode" label="validate">功能验证</el-radio>
                <el-radio v-model="mode" label="benchmark">性能验证</el-radio>
            </div>
            <template v-if="mode === 'benchmark'">
                <div class="tcr">
                    <el-input v-model="tcr" style="max-width: 600px" placeholder="压测参数">
                        <template #prepend>
                            <span class="input-prepend">压测参数：</span>
                        </template>
                    </el-input>
                </div>
                <div class="ops">
                    <el-input v-model="ops" style="max-width: 600px" placeholder="目标查询">
                        <template #prepend>
                            <span class="input-prepend">目标查询：</span>
                        </template>
                    </el-input>
                </div>
            </template>
        </div>
    </div>
</template>
<script setup lang="ts">
import { ref, reactive, watch } from 'vue'
import type { Ref } from 'vue'
import type { ModeInfo } from '../type'
import { useRunviewStore } from '@/stores/runview';
const runviewStore = useRunviewStore()
// 定义 mode、tcr、ops
const mode: Ref<'validate' | 'benchmark'> = ref('validate')
const tcr: Ref<number> = ref(0.01)
const ops: Ref<number> = ref(18000)
mode.value = runviewStore.modeInfo.mode
tcr.value = runviewStore.modeInfo.mode === 'benchmark' ? runviewStore.modeInfo.tcr : tcr.value
ops.value = runviewStore.modeInfo.mode === 'benchmark' ? runviewStore.modeInfo.ops : ops.value
// 监听 data 的变化，并更新 Pinia store 中的 dataInfo.data
// 同时监听 mode、tcr 和 ops 的变化
watch([mode, tcr, ops], ([newMode, newTcr, newOps]) => {
    // 根据 mode 的新值决定如何更新 Pinia store
    if (newMode === 'validate') {
        runviewStore.updateModeInfo({ mode: newMode })
    } else {
        runviewStore.updateModeInfo({ mode: newMode, tcr: newTcr, ops: newOps })
    }
})
</script>

<style scoped lang="less">
.finbech-modeinfo {
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
        background-image: url('../assets/mode.png');
        background-size: contain;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .tcr {
        grid-column-start: 1;
        grid-column-end: 3;
    }

    .ops {
        grid-column-start: 1;
        grid-column-end: 3;
    }
}
</style>