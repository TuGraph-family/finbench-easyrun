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
  </div>
</template>

<script setup lang="ts">
import Header from '../components/Header.vue'
import SystemInfo from '@/components/SystemInfo.vue';
import DataInfo from '@/components/DataInfo.vue';
import ModeInfo from '@/components/ModeInfo.vue';
</script>

<style scoped lang="less">
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
</style>