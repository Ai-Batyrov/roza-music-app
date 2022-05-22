<template>
   <div class="page">
      <div class="headline">
         <h2>Search</h2>
      </div>
      <div class="search-input">
         <input type="text" v-model="inputText">
         <button
            type="submit"
            class="search-button"
            @click="search"
         >Search
         </button>
      </div>
      <div class="search-results">
         <Suspense>
            <!--            <template #default>-->
            <!--               <PlaylistItem/>-->
            <!--            </template>-->
            <template #default>
               <PlaylistItemSkeleton/>
            </template>
         </Suspense>
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
         inputText: String,
         resultList: []
      }
   },
   methods: {
      async search(text) {
         await axios
            .get('/api/v1/search-song/' + text)
            .then()
      }
   }
}
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";

.page {
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
