<template>
   <div class="chart-playlist">
      <h3>{{ playlist.title }}</h3>
      <div class="playlist-div">
         <PlaylistItem
            v-for="track in trackList"
            :title="track.title"
            :artist="track.artist"
            :track="track.id"
         />
      </div>
   </div>
</template>

<script>
import axios from "axios";
import PlaylistItem from "@/components/playlist/PlaylistItem";

export default {
   name: "PlaylistView",
   components: {PlaylistItem},
   data() {
      return {
         playlist: [],
         trackList: []
      };
   },
   async mounted() {
      await this.getPlaylist()
      this.getTracks()
   },
   methods: {
      getPlaylist() {
         return new Promise(resolve => {
            axios
               .get('/api/v1/get/playlist/' + this.$route.params.id)
               .then(response => {
                  resolve(this.playlist = response.data)
               })
               .catch(error => {
                  console.log(error);
               });
         })
      },
      getTracks() {
         for (const track_id in this.playlist.tracks) {
            axios
               .get('/api/v1/track/' + this.playlist.tracks[track_id])
               .then(response => {
                  this.trackList.push(response.data)
               })
               .catch(error => {
                  console.log(error)
               })
         }
      }
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";

.chart-playlist {
   width: 100%;
   height: 60%;
   .flex-column-direction();
   .global-font();
}

h4 {
   width: 100%;
}

.playlist-div {
   width: 100%;
   height: 95%;
   display: flex;
   flex-direction: column;
}
</style>
