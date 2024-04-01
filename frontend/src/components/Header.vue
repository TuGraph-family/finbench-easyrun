<template>
  <div class="finbench-header">
    GraphBench图数据库基准测试系统
    <div @click="jumpto">
      <span>Powerby</span>
      <img src="../assets/logo.png" alt="">
    </div>

  </div>
</template>
<script setup lang="ts">
function jumpto() {
  window.open('https://tugraph.tech/')
}
</script>

<style scoped lang="less">
.finbench-header {
  height: 60px;
  /* 高度为视口高度的20% */
  line-height: 60px;
  text-align: center;
  font-size: 30px;
  font-weight: 700;
  position: relative;
  border-bottom: 5px solid #ddd;

  div {
    position: absolute;
    display: flex;
    width: 120px;
    flex-grow: 0;
    cursor: pointer;
    right: 25px;
    top: 10px;
  }

  span {
    font-size: 16px;
    font-style: italic;
    background: linear-gradient(to right, #1651ff, #16c6ff);
    background-clip: text;
    /* 标准的背景剪裁属性，仅显示文字部分 */
    color: transparent;
    /* 设置文字颜色为透明，以便显示渐变背景 */
    display: inline-block;
    /* 设置为内联块元素，以便背景正确应用到文字上 */
  }

  img {
    width: 90px;
    height: auto;
    object-fit: contain
  }
}
</style>
