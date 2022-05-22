<template>
   <div class="control">
      <img :src="iconUrl" alt="control-icon"/>
   </div>
</template>

<script>
export default {
   name: "Control",
   props: {
      iconUrl: String
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";

.control {
   width: 3rem;
   height: 3rem;
   border-radius: 0.3rem;
   .centering();
   background-color: #E6ECFF;
   margin: 0 0 0 0.7rem;
   cursor: pointer;
   transition: all 0.3s ease-in-out;

   img {
      width: 1.2rem;
   }

   &:hover {
      background-color: #b8d2e5;
   }
}
</style>
