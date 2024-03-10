<template>
    <div class="finbech-datainfo">
        <div class="finbech-datainfo-title">数据配置</div>
        <div class="finbech-datainfo-img"></div>
    </div>
</template>
<script setup lang="ts">

</script>

<style scoped lang="less">
.finbech-datainfo {
    width: 100%;

    &-title {
        font-weight: bolder;
        font-size: 18px;
        padding: 3px 10px;
        border-bottom: 1px solid #ddd;
    }

    &-img {
        margin: 10px;
        width: 100px;
        height: 100px;
        background-image: url('../assets/data.png');
        background-size: contain;
    }
}
</style>