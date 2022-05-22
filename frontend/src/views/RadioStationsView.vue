<template>
   <div class="radio-stations-page">
      <div class="radio-stations-playlist-view">
         <div class="headline">
            <h2>Radio stations</h2>
         </div>
         <div class="playlist-div">
            <RadioPlaylistItem
               v-for="radio in radioStationsList"
               :title="radio.title"
               :artist="radio.broadcast_url"
               :radio_id="radio.id"
            />
         </div>
      </div>

   </div>
</template>

<script>
import axios from "axios";
import PlaylistItem from "@/components/playlist/PlaylistItem";
import RadioPlaylistItem from "@/components/playlist/RadioPlaylistItem";

export default {
   name: "RadioStationsView",
   components: {RadioPlaylistItem, PlaylistItem},
   data() {
      return {
         radioStationsList: []
      }
   },
   async mounted() {
      await this.getRadioStations()
   },
   methods: {
      getRadioStations() {
         return new Promise(resolve => {
            axios
               .get('/api/v1/radiostations/')
               .then(response => {
                  resolve(this.radioStationsList = response.data)
               })
               .catch(error => {
                  console.log(error);
               });
         })
      },
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";

.radio-stations-page {
   width: 100%;
   height: 100%;
}

.radio-stations-playlist-view {
   width: 100%;
   height: 100%;
   display: flex;
   flex-direction: column;
   justify-content: space-between;
   align-items: flex-start;
}

h2 {
   .global-font();
}

.playlist-div {
   width: 100%;
   height: 95%;
   display: flex;
   flex-direction: column;
}
</style>
