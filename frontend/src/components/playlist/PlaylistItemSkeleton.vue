<template>
   <div class="item">
      <div class="cover-div">
         <button
            class="cover-play-span"
         >
         </button>
      </div>
      <div class="title-div">
         <p class="p-title">
         </p>
         <p class="p-artist">
         </p>
      </div>
      <div class="like-div">
      </div>
   </div>
</template>

<script>
export default {
   name: "PlaylistItemSkeleton"
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";
@import "@/assets/css/playlist-item.less";

.item {
   background-color: #CCEDFF !important;
}

.cover-play-span {
   background-color: #E6ECFF !important;
}
</style>
