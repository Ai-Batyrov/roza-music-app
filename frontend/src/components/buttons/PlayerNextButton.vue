<template>
   <div class="button-div">
      <button type="button" class="button-class">
         <img :src="BtnUrl" alt="control-btn"/>
      </button>
   </div>
</template>

<script>
import BtnUrl from "@/assets/player/next 1.svg"

export default {
   name: "PlayerNextButton",
   data() {
      return {
         BtnUrl
      }
   }
}
</script>


<style lang="less" scoped>
@import "@/assets/css/player-control-btns.less";

</style>
