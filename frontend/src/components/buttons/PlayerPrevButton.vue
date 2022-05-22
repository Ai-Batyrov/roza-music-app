<template>
   <div class="button-div">
      <button type="button" class="button-class">
         <img :src="BtnUrl" alt="control-btn"/>
      </button>
   </div>
</template>

<script>
import BtnUrl from "@/assets/player/next 2.svg"

export default {
   name: "PlayerPrevButton",
   data() {
      return {
         BtnUrl
      }
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/player-control-btns.less";

.button-div {
   .button-div();
}

.button-class {
   .button-class();
}
</style>
