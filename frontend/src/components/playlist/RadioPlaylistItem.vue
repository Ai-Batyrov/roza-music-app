<template>
   <div class="item">
      <div class="cover-div">
         <button
            class="cover-play-span"
            @click="playItem"
            v-if="!isPlaying"
         >
            <img :src="play_btn" alt="play-btn"/>
         </button>
         <button
            class="cover-play-span pause-btn"
            v-else
            @click="pause"
         >
            <img :src="pause_btn" alt="play-btn"/>
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
   </div>
</template>

<script>
import play_btn from '@/assets/playlist/play 1.svg'
import like_btn from '@/assets/playlist/like 2.svg'
import pause_btn from '@/assets/player/pause.svg'
import store from "@/store";
import axios from "axios";

export default {
   name: "RadioPlaylistItem",
   data() {
      // let broadcast_url = this.artist
      return {
         play_btn, like_btn, pause_btn,
         player: new Audio(),
         index: 0,
         isPlaying: false,
         playlist: [],
         url: this.radio_id
      }
   },
   props: {
      title: String,
      artist: String,
      radio_id: Number
   },
   methods: {
      play(track) {
         this.playlist[0] = track
         this.player.src = this.playlist[0].broadcast_url
         this.player.play()
         this.isPlaying = true
      },
      pause() {
         this.player.pause()
         this.isPlaying = false
      },
      async playItem() {
         await this.getRadio()
         this.play(this.playlist[0])
      },
      getRadio() {
         return new Promise(resolve => {
            axios
               .get('/api/v1/radiostation/' + this.url)
               .then(response => {
                  resolve(this.playlist[0] = response.data)
               })
               .catch(error => {
                  console.log(error);
               });
         })
      },
   },
}
</script>

<style lang="less" scoped>
@import "@/assets/css/playlist-item.less";

.pause-btn {
   img {
      filter: hue-rotate(380deg) !important;
      display: block !important;
   }
}
</style>
