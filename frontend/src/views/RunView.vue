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
      <Result />
    </div>
  </div>
</template>

<script setup lang="ts">
import Header from '../components/Header.vue'
import SystemInfo from '@/components/SystemInfo.vue';
import DataInfo from '@/components/DataInfo.vue';
import ModeInfo from '@/components/ModeInfo.vue';
import Progress from '@/components/Progress.vue';
import Result from '@/components/Result.vue';
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

.run-result {
  margin-top: 20px;
  border: 1px solid #ddd;
  flex: 1;
  border: 5px solid #ddd;
  border-radius: 8px;
}
</style>