<template>
    <div class="finbech-systeminfo">
        <div class="finbech-systeminfo-title">系统配置

            <el-icon @click="openDialog">
                <Setting />
            </el-icon>
        </div>
        <div class="finbech-systeminfo-container">
            <div class="finbech-systeminfo-img"></div>
            <div>
                <div>机型：</div>
                <div class="parameters">{{ runviewStore.systemInfo.model }}</div>
            </div>
            <div>
                <div>系统：</div>
                <div class="parameters">{{ runviewStore.systemInfo.os }}</div>
            </div>
            <div>
                <div>处理器：</div>
                <div class="parameters">{{ runviewStore.systemInfo.cpu }}</div>
            </div>
            <div>
                <div>内存：</div>
                <div class="parameters">{{ runviewStore.systemInfo.memory }}</div>
            </div>
            <div>
                <div>硬盘：</div>
                <div class="parameters">{{ runviewStore.systemInfo.storage }}</div>
            </div>
            <div>
                <div>网络：</div>
                <div class="parameters">{{ runviewStore.systemInfo.network }}</div>
            </div>
        </div>
        <el-dialog destroy-on-close v-model="dialogVisible" title="系统配置" width="500">
            <div>
                <img src="../assets/system.png" alt="">
                <el-input v-model="systemInfo.model" style="max-width: 600px" placeholder="机型信息">
                    <template #prepend>
                        <span class="input-prepend">机型：</span>
                    </template>
                </el-input>
                <el-input v-model="systemInfo.os" style="max-width: 600px" placeholder="系统信息">
                    <template #prepend>
                        <span class="input-prepend">系统：</span>
                    </template>
                </el-input>
                <el-input v-model="systemInfo.cpu" style="max-width: 600px" placeholder="处理器信息">
                    <template #prepend>
                        <span class="input-prepend">处理器：</span>
                    </template>
                </el-input>
                <el-input v-model="systemInfo.memory" style="max-width: 600px" placeholder="内存信息">
                    <template #prepend>
                        <span class="input-prepend">内存：</span>
                    </template>
                </el-input>
                <el-input v-model="systemInfo.storage" style="max-width: 600px" placeholder="硬盘信息">
                    <template #prepend>
                        <span class="input-prepend">硬盘：</span>
                    </template>
                </el-input>
                <el-input v-model="systemInfo.network" style="max-width: 600px" placeholder="网络信息">
                    <template #prepend>
                        <span class="input-prepend">网络：</span>
                    </template>
                </el-input>
            </div>
            <template #footer>
                <div class="dialog-footer">
                    <el-button @click="dialogVisible = false">取消</el-button>
                    <el-button type="primary" @click="updateInfo">
                        确认
                    </el-button>
                </div>
            </template>
        </el-dialog>
    </div>
</template>
<script setup lang="ts">
import { ref, reactive } from 'vue'
import { useRunviewStore } from '../stores/runview'
import type { SystemInfo } from '../type'
import { ElMessageBox } from 'element-plus'
const runviewStore = useRunviewStore()
const dialogVisible = ref(false)
const systemInfo = reactive<SystemInfo>({
    model: '',
    os: '',
    cpu: '',
    memory: '',
    storage: '',
    network: ''
})
function updateInfo() {
    runviewStore.updateSystemInfo(systemInfo);
    dialogVisible.value = false
}
function openDialog() {
    Object.assign(systemInfo, runviewStore.systemInfo)
    dialogVisible.value = true

}
</script>

<style scoped lang="less">
.finbech-systeminfo {
    width: 100%;

    &-title {
        font-weight: bolder;
        font-size: 18px;
        padding: 3px 10px;
        border-bottom: 1px solid #ddd;
        position: relative;

        .el-icon {
            position: absolute;
            right: 10px;
            bottom: 5px;
            cursor: pointer;
        }
    }

    &-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: repeat(4, 1fr);
        padding: 10px;

        >div {
            margin: 0 10px 10px 0;
        }
    }

    &-img {
        width: 100px;
        height: 110px;
        background-image: url('../assets/system.png');
        background-size: contain;
        background-repeat: no-repeat;
        grid-row-start: 1;
        grid-row-end: 3;
    }

    .el-input {
        margin-bottom: 10px;

        &:last-child {
            margin-bottom: 0;
        }
    }

    .input-prepend {
        width: 60px;
        /* 根据需要调整这个宽度 */
        display: inline-block;
        /* 保证可以应用宽度 */
        text-align: right;
        /* 右对齐文本 */
    }

    img {
        width: 150px;
        display: block;
        margin: 0 auto 10px auto;
    }
}
</style>