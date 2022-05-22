<template>
   <div class="chart-playlist">
      <h3>{{ tracksInChart.title }}</h3>
      <div class="playlist-div">
         <PlaylistItem
            v-for="track in tracksList"
            :title="track.title"
            :artist="track.artist"
            :track="track.id"
         />
      </div>
   </div>
</template>

<script>
import PlaylistItem from "@/components/playlist/PlaylistItem";
import axios from "axios";

export default {
   name: "ChartPlaylistView",
   components: {PlaylistItem},
   data() {
      return {
         tracksInChart: [],
         tracksList: []
      }
   },
   async mounted() {
      await this.getTracksInChart()
      this.getTrack()
   },
   methods: {
      getTracksInChart() {
         return new Promise(resolve => {
            axios
               .get('/api/v1/chart/' + this.$route.params.id)
               .then(response => {
                  resolve(this.tracksInChart = response.data)
               })
               .catch(error => {
                  console.log(error);
               });
         })
      },
      getTrack() {
         for (const track_id in this.tracksInChart.tracks) {
            axios
               .get('/api/v1/track/' + this.tracksInChart.tracks[track_id])
               .then(response => {
                  this.tracksList.push(response.data)
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
