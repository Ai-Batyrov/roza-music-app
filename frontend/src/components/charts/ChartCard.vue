<template>
   <div class="card">
      <div class="card-inner">

      </div>
   </div>
</template>

<script>
export default {
   name: "ChartCard"
}
</script>

<style scoped lang="less">
@import "@/assets/css/style.less";

.card {
   width: 15rem;
   height: 20rem;
   .centering();
}

.card-inner {
   width: 95%;
   height: 95%;
   .flex-column-direction();
}
</style>
