<template>
    <div class="finbech-modeinfo">
        <div class="finbech-modeinfo-title">模式配置</div>
        <div class="finbech-modeinfo-container">
            <div class="finbech-modeinfo-img"></div>

        </div>

    </div>
</template>
<script setup lang="ts">

</script>

<style scoped lang="less">
.finbech-modeinfo {
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
        background-image: url('../assets/mode.png');
        background-size: contain;
    }
}
</style>