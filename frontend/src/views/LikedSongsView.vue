<template>
   <div class="liked-songs-page">
      <div class="headline">
         <h2>Liked Songs</h2>
      </div>
      <div class="playlist-div">
         <TransitionGroup
            tag="div"
            name="list"
            appear
         >
            <PlaylistItem
               v-for="result in trackPlaylist"
               :title="result.title"
               :artist="result.artist"
               :track="result.id"
               :key="result.id"
            />
         </TransitionGroup>
      </div>
   </div>
</template>

<script>
import axios from "axios";
import PlaylistItem from "@/components/playlist/PlaylistItem";

export default {
   name: "LikedSongsView",
   components: {PlaylistItem},
   data() {
      return {
         likedSongsList: [],
         trackPlaylist: []
      }
   },
   async mounted() {
      await this.getLikedSongs()
      this.getTracks()
   },
   methods: {
      getLikedSongs() {
         return new Promise(resolve => {
            axios
               .get('api/v1/likedsongs/')
               .then(response => {
                  resolve(this.likedSongsList = response.data)
               })
         })
      },
      getTracks() {
         this.likedSongsList.map(index => {
               axios.get('/api/v1/track/' + index.track)
                  .then(response => {
                     this.trackPlaylist.push(response.data)
                  })
                  .catch(error => {
                     console.log(error)
                  })
            }
         )
      }
   },
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";
@import "@/assets/css/playlist-item.less";
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1";

.liked-songs-page {
   width: 100%;
   height: 100%;
   display: flex;
   flex-direction: column;
}

.headline {
   width: 100%;
   height: 5%;
   .global-font();
   user-select: none;
}

.playlist-div > div {
   width: 100%;
   height: 80%;
   display: flex;
   flex-direction: column;
   padding: 1rem 0 0 0;
}

.list-enter-active,
.list-leave-active {
   transition: all 1s ease;
}

.list-enter-from,
.list-leave-to {
   opacity: 0;
   transform: translateX(30px);
}
</style>
