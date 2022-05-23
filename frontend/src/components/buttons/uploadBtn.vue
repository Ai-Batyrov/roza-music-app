<template>
   <div class="upload-btn">
      <div class="inner">
         <img :src="BtnIcon" alt="add-playlist-btn"/>
         <p>Upload track</p>
      </div>
   </div>
</template>

<script>
import BtnIcon from "@/assets/uploadTrack.svg"

export default {
   name: "uploadBtn",
   data() {
      return {
         BtnIcon
      }
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";

.upload-btn {
   width: 10rem;
   height: 3rem;
   border-radius: 0.3rem;
   .centering();
   background-color: #E6ECFF;
   cursor: pointer;
   transition: all 0.3s ease-in-out;

   img {
      width: 1.2rem;
   }

   &:hover {
      background-color: #b8d2e5;
   }
}

.inner {
   width: 80%;
   height: 100%;
   display: flex;
   align-items: center;
   justify-content: space-between;
   user-select: none;

   img {
      width: 2rem;
   }

   p {
      .global-font();
      font-size: 0.85rem;
   }
}
</style>
