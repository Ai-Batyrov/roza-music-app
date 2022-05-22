<template>
   <div class="page">
      <div class="headline">
         <h2>Search</h2>
      </div>
      <div class="search-input">
         <q-input outlined v-model="text" :dense="dense"/>
         <button type="submit">Search</button>
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

export default {
   name: "SearchView",
   components: {PlaylistItemSkeleton, PlaylistItem}
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
   width: 100%;
   height: 10%;
   display: flex;
   justify-content: flex-start;
   align-items: center;
}

.search-results {
   width: 100%;
   height: 80%;
}
</style>
