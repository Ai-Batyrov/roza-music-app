<template>
   <div class="search-page">
      <div class="headline">
         <h2>Search</h2>
      </div>
      <div class="search-input">
         <input type="text" v-model="inputText">
         <button
            type="submit"
            class="search-button"
            @click="search(inputText)"
         >Search
         </button>
      </div>
      <div class="search-results">
         <PlaylistItem
            v-for="result in allTracksList"
            :title="result.title"
            :artist="result.artist"
            :track="result.id"
         />
      </div>
   </div>
</template>

<script>
import PlaylistItem from "@/components/playlist/PlaylistItem";
import PlaylistItemSkeleton from "@/components/playlist/PlaylistItemSkeleton";
import axios from "axios";

export default {
   name: "SearchView",
   components: {PlaylistItemSkeleton, PlaylistItem},
   data() {
      return {
         inputText: "",
         resultList: [],
         allTracksList: []
      }
   },
   async mounted() {
      await this.getAllTracks()
   },
   methods: {
      search(text) {

      },
      getAllTracks() {
         return new Promise(resolve => {
            axios
               .get('api/v1/get/all-tracks')
               .then(response => {
                  resolve(this.allTracksList = response.data)
               })
               .catch(error => {
                  console.log(error)
               })
         })
      }
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";

.search-page {
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

.search-input {
   width: 70%;
   height: 10%;
   display: flex;
   justify-content: space-between;
   align-items: center;
}

.search-results {
   width: 100%;
   height: 80%;
   display: flex;
   flex-direction: column;
   padding: 1rem 0 0 0;
}

input {
   width: 80%;
   height: 2rem;
   .global-font();
}

.search-button {
   width: 5rem;
   height: 2.5rem;
   border: none;
   background-color: #b8d2e5;
   border-radius: 0.3rem;
   transition: all 0.2s ease-in-out;
   .global-font();
   cursor: pointer;

   &:hover {
      background-color: #E6ECFF;
   }

   &:active {
      background-color: #90a4b2;
   }
}
</style>
