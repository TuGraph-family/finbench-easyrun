<template>
  <div class="run">
    <div>
      <Header />
    </div>
    <div>
      <SystemInfo />
    </div>
    <div v-if="isSystemInfoComplete">
      <ModeInfo />
    </div>
    <div>
      <Progress />
    </div>
    <div style="height: calc(100% - 470px);">
      <Logs />
    </div>
    <div v-if="isCompleted" class="result-btn">
      <el-button v-if="mode == 'benchmark'" size="large" type="success" @click="open">查看结果</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">

import { computed } from 'vue'
import Header from '../components/Header.vue'
import SystemInfo from '@/components/SystemInfo.vue'
import ModeInfo from '@/components/ModeInfo.vue'
import Progress from '@/components/Progress.vue'
import Logs from '@/components/Logs.vue'
import { useRunviewStore } from '../stores/runview'
import { useRouter } from 'vue-router';
const router = useRouter();
const runviewStore = useRunviewStore()
const isSystemInfoComplete = computed(() => {
  const { model, os, cpu, memory, storage, network } = runviewStore.systemInfo
  return model || os || cpu || memory || storage || network
})
const isSystemStart = computed(() => {
  const { uuid } = runviewStore.systemStatus
  return !!uuid
})
const isCompleted = computed(() => {
  const { status } = runviewStore.progressResult
  return status === 'Completed' ? true : false
})

const mode = computed(() => {
  const { mode } = runviewStore.modeInfo
  return mode
})

function open() {
  router.push({ name: 'resultview' });
}

</script>

<style scoped lang="less">
.run {
  width: 100%;
  height: 100%;

  .result-btn {
    position: absolute;
    bottom: 10px;
    right: 0px;
    padding: 0 1.875rem;
    display: flex;
    justify-content: flex-end;

    .el-button {
      width: 200px;
    }
  }
}
</style>