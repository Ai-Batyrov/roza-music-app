<template>
   <div class="button-div">
      <button type="button" class="button-class">
         <img :src="BtnUrl" alt="control-btn"/>
      </button>
   </div>
</template>

<script>
import BtnUrl from "@/assets/player/pause.svg"

export default {
   name: "PlayerPauseButton",
   data() {
      return {
         BtnUrl
      }
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/player-control-btns.less";
@import "@/assets/css/style.less";

.button-div {
   width: 3rem;
   height: 3rem;
}

.button-class {
   width: 100%;
   height: 100%;
   border: none;
   border-radius: 50%;
   transition: all 0.3s ease-in-out;
   cursor: pointer;
   .centering();
   background-color: #E6ECFF;

   img {
      width: 1.1rem;
   }

   &:hover {
      background-color: #b9d0e0;

      img {
         filter: invert(0.3);
      }
   }

   &:active {
      background-color: #90a4b2;
   }
}
</style>
