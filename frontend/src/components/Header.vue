<template>
  <div class="header-component">
    <div class="logo">
      <img  :src="logoSrc" alt="">
    </div>
    <div class="header-title">
      {{ headerName }}
    </div>
  </div>
</template>
<script setup lang="ts">
import { HEADERCONFIG } from '../config/config'
import {getAssetsFile} from '../utils/util'
const headerName =  `${HEADERCONFIG.headerName} 图数据库基准测试系统`

const logoSrc = getAssetsFile('',HEADERCONFIG.imageName)
document.title = headerName 
</script>

<style scoped lang="less">
.header-component {
  height: 10rem;
  overflow: hidden;
  .logo {
    height: 3.75rem;
    background-color: #333333;
    img{
      height: 100%;
      width: auto;
      padding:0 1.875rem;
      background-color: #fff;
    }
    
  }
  .header-title{
    font-size: 1.4rem;
    line-height: 6.25rem;
    text-align: center;
  }
}
</style>
