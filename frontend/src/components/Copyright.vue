<template>
   <div>
      <span>
         All rights reserved <strong>ROZA Inc.</strong>
      </span>
   </div>
</template>

<script>
export default {
   name: "Copyright"
}
</script>

<style scoped lang="less">
@import "@/assets/css/style.less";

div {
   width: 100%;
   height: 3rem;
   .centering();
}

span {
   .global-font();
   user-select: none;
   opacity: 0.6;
}
</style>
