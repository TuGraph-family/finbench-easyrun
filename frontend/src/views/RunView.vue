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
  </div>
</template>

<script setup lang="ts">

import { ref, computed } from 'vue'
import Header from '../components/Header.vue'
import SystemInfo from '@/components/SystemInfo.vue';
import ModeInfo from '@/components/ModeInfo.vue';
import { useRunviewStore } from '../stores/runview'
const runviewStore = useRunviewStore()
const isSystemInfoComplete = computed(() => {
    const { model, os, cpu, memory, storage, network } = runviewStore.systemInfo
    return model && os && cpu && memory && storage && network
})
</script>

<style scoped lang="less">
.run {
}


</style>