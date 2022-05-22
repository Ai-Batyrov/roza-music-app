<template>
   <div class="user-div">
      <img :src="userIcon" alt="user-icon"/>
   </div>
</template>

<script>
import userIcon from "@/assets/controls/user-icon.svg"

export default {
   name: "UserControl",
   data() {
      return {
         userIcon
      }
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";

.user-div {
   width: 3rem;
   height: 3rem;
   border-radius: 50%;
   .centering();
   background-color: #E6ECFF;
   cursor: pointer;
   margin: 0 0 0 0.7rem;
   transition: all 0.3s ease-in-out;

   img {
      width: 1.6rem;
   }

   &:hover {
      background-color: #b8d2e5;
   }
}
</style>
