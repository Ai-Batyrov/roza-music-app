<template>
   <div class="button">
      {{ name }}
   </div>
</template>

<script>
export default {
   name: "CardButtons",
   props: {
      name: String
   }
}
</script>

<style scoped lang="less">
@import "@/assets/css/style.less";

.button {
   width: 3.4rem;
   height: 2rem;
   .centering();
   .global-font();
   border-radius: 0.3rem;
   background-color: #A3BBC8;
   color: #243F4D;
   transition: all 0.3s ease-in-out;

   &:hover {
      background-color: #b8d2e5;
   }
}
</style>
