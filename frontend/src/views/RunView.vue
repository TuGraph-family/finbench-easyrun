<template>
  <div class="run">
    <Header />
    <div class="run-parameters">
      <div class="system">
        <SystemInfo />
      </div>
      <div class="data">
        <DataInfo />
      </div>
      <div class="mode">
        <ModeInfo />
      </div>
    </div>
    <div class="run-progress">
      <Progress />
    </div>
    <div class="run-result">
      <div v-if="proStatus === 'finished'">
        <Result />
      </div>
      <div v-else>
        暂无结果
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">

import { ref, computed } from 'vue'
import Header from '../components/Header.vue'
import SystemInfo from '@/components/SystemInfo.vue';
import DataInfo from '@/components/DataInfo.vue';
import ModeInfo from '@/components/ModeInfo.vue';
import Progress from '@/components/Progress.vue';
import Result from '@/components/Result.vue';

import { useRunviewStore } from '@/stores/runview';
const runviewStore = useRunviewStore()
let proStatus = computed(() => runviewStore.progressResult.status)
</script>

<style scoped lang="less">
.run {
  display: flex;
  flex-direction: column;
  height: calc(100% - 20px);
  padding-bottom: 20px;
}

.run-parameters {
  width: 100%;
  display: flex;
  padding: 20px 0;

  >div {
    flex: 1;
    margin-right: 20px;
    height: 270px;
    border: 5px solid #ddd;
    border-radius: 8px;
  }

  div:last-child {
    margin-right: 0;
  }
}

.run-progress {
  border: 5px solid #ddd;
  border-radius: 8px;
  height: 100px;
}
</style>