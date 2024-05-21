<template>
    <div class="result">
        <div class="result-header">
            <el-button type="primary" plain :icon="Back" @click="back">返回</el-button>
        </div>
        <div class="result-container">
            <Result />
        </div>
    </div>
</template>
<script setup lang="ts">
import Result from '@/components/Result.vue'
import {
  Back
} from '@element-plus/icons-vue'
import { useRouter } from 'vue-router';
import { useRunviewStore } from '../stores/runview'
const router = useRouter();
const runviewStore = useRunviewStore()
async function getResult(){
  const { uuid } = runviewStore.systemStatus
  let res:any
  if(uuid !== 'test_uuid'){
    res = await runviewStore.getResult(uuid)
  }else{
    res = await runviewStore.getTestResult(uuid)
  }
  runviewStore.updateResult(res)
}
function back(){
  router.push({ name: 'easyrun' });
}
if(runviewStore.progressResult.phase === 'completed'){
  getResult()
}
</script>
<style lang="less" scoped>
.result {
    .result-header {
      height: 3.75rem;
      background-color: #333333;
      padding-left: 1.875rem;
      display: flex;
      align-items: center;
    }
    .header-title{
      font-size: 1.4rem;
      line-height: 6.25rem;
      text-align: center;
    }
    .result-container{
        padding:0 1.875rem;
    }
  }
</style>