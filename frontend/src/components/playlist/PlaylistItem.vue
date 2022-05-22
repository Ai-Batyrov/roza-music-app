<template>
   <div class="item">
      <div class="cover-div">
         <button
            class="cover-play-span"
            @click="playItem(track_id)"
         >
            <img :src="play_btn" alt="play-btn"/>
         </button>
      </div>
      <div class="title-div">
         <p class="p-title">
            {{ title }}
         </p>
         <p class="p-artist">
            {{ artist }}
         </p>
      </div>
      <div class="like-div">
         <img :src="like_btn" alt="like-btn"/>
      </div>
   </div>
</template>

<script>
import play_btn from '@/assets/playlist/play 1.svg'
import like_btn from '@/assets/playlist/like 2.svg'
import store from "@/store";
import player from "@/assets/js/Player";
import {readonly} from "vue";

export default {
   name: "PlaylistItem",
   props: {
      title: String,
      artist: String,
      track: Number
   },
   data() {
      let track_id = this.track
      return {
         play_btn, like_btn, track_id
      }
   },
   methods: {
      async playItem(track_id) {
         await store
            .dispatch("playItem", track_id)
      }
   }
}
</script>

<style scoped lang="less">
@import "@/assets/css/style.less";
@import "@/assets/css/playlist-item.less";

</style>
