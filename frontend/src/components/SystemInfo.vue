<template>
    <div class="systeminfo">
        <div class="systeminfo-title">系统配置
            <el-icon @click="openDialog" style="color: #fff;">
                <Setting />
            </el-icon>
        </div>
        <div v-if="isSystemInfoComplete" class="systeminfo-container">
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
        <div v-else class="systeminfo-null">
            暂无系统配置
        </div>
        <el-dialog destroy-on-close v-model="dialogVisible" title="系统配置" width="500">
            <el-form ref="ruleFormRef" :inline="true" :model="systemInfoData" label-width="auto">
                <el-form-item label="机型" prop="model">
                    <el-input v-model="systemInfoData.model" style="max-width: 600px" placeholder="机型信息"></el-input>
                </el-form-item>
                <el-form-item label="系统" prop="os">
                    <el-input v-model="systemInfoData.os" style="max-width: 600px" placeholder="系统信息"></el-input>
                </el-form-item>
                <el-form-item label="处理器" prop="cpu">
                    <el-input v-model="systemInfoData.cpu" style="max-width: 600px" placeholder="处理器信息"></el-input>
                </el-form-item>
                <el-form-item label="内存" prop="memory">
                    <el-input v-model="systemInfoData.memory" style="max-width: 600px" placeholder="内存信息"></el-input>
                </el-form-item>
                <el-form-item label="硬盘" prop="storage">
                    <el-input v-model="systemInfoData.storage" style="max-width: 600px" placeholder="硬盘信息"></el-input>
                </el-form-item>
                <el-form-item label="网络" prop="network">
                    <el-input v-model="systemInfoData.network" style="max-width: 600px" placeholder="网络信息"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <div class="dialog-footer">
                    <el-button v-if="isReseting" loading :disabled="true" type="danger">重置系统</el-button>
                    <el-button v-else="isReseting" @click="resetSystem()" type="danger">重置系统</el-button>
                    <el-button @click="resetForm(ruleFormRef)">取消</el-button>
                    <el-button type="primary" @click="submitForm(ruleFormRef)"> 确认</el-button>
                </div>
            </template>
        </el-dialog>
    </div>
</template>
<script setup lang="ts">
import { ref, reactive, computed } from 'vue'
import { useRunviewStore } from '../stores/runview'
import type { SystemInfo } from '../type'
import type { FormRules, FormInstance } from 'element-plus'
const runviewStore = useRunviewStore()
const dialogVisible = ref(false)
const ruleFormRef = ref<FormInstance>()
const systemInfoData = reactive<SystemInfo>({
    model: '',
    os: '',
    cpu: '',
    memory: '',
    storage: '',
    network: ''
})
const rules = reactive<FormRules<SystemInfo>>({
    model: [
        { required: true, message: '请填写机型信息', trigger: 'blur' },
    ],
    os: [
        { required: true, message: '请填写系统信息', trigger: 'blur' },
    ],
    cpu: [
        { required: true, message: '请填写处理器信息', trigger: 'blur' },
    ],
    memory: [
        { required: true, message: '请填写内存信息', trigger: 'blur' },
    ],
    storage: [
        { required: true, message: '请填写硬盘信息', trigger: 'blur' },
    ],
    network: [
        { required: true, message: '请填写网络信息', trigger: 'blur' },
    ],
})
const isReseting = computed(() => {
    return runviewStore.isReseting
})
const isSystemInfoComplete = computed(() => {
    const { model, os, cpu, memory, storage, network } = runviewStore.systemInfo
    return model || os || cpu || memory || storage || network
})

function openDialog() {
    Object.assign(systemInfoData, runviewStore.systemInfo)
    dialogVisible.value = true

}
const submitForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.validate((valid) => {
        if (valid) {
            runviewStore.updateSystemInfo(systemInfoData);
            dialogVisible.value = false
        } else {
            console.log('error submit!')
        }
    })
}

const resetForm = (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.resetFields()
}
async function resetSystem() {
    runviewStore.updateIsReseting(true)
    await runviewStore.resetAll();
    runviewStore.updateIsReseting(false)
}

</script>

<style scoped lang="less">
.systeminfo {
    padding: 0 1.875rem 0.875rem 1.875rem;
    width: calc(100% - 3.75rem);

    .systeminfo-title {
        display: flex;
        align-items: center;
        justify-content: space-between;
        font-weight: 700;
        line-height: 40px;
        border-bottom: 1px dotted #424242;
        font-size: 1.125rem;

        .el-icon {
            cursor: pointer;
        }
    }

    .systeminfo-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-template-rows: repeat(2, auto);
        gap: 10px;
        margin-top: 10px;

        >div {
            display: flex;
            align-items: center;
        }
    }

    .systeminfo-null {
        height: 3.75rem;
        line-height: 3.75rem;
        text-align: center;
    }

    .el-form-item {
        width: 100%;
    }
}
</style>