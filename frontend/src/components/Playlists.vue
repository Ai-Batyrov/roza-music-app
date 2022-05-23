<template>
   <div v-for="playlist in playlists">
      <MenuButton
         :menu_name="playlist.title"
         :router_link="'/playlist/' + playlist.id"
         :icon-url="iconUrl"
      >
      </MenuButton>
   </div>
</template>

<script>
import axios from "axios";
import MenuButton from "@/components/MenuButton";
import iconUrl from "@/assets/menu/playlist.svg"

export default {
   name: "Playlists",
   components: {
      MenuButton
   },
   data() {
      return {
         playlists: [],
         iconUrl
      };
   },
   mounted() {
      this.getPlaylists()
   },
   methods: {
      getPlaylists() {
         axios
            .get('/api/v1/playlists/')
            .then(response => {
               this.playlists = response.data
            })
            .catch(error => {
               console.log(error);
            });
      }
   }
}
</script>

<style scoped>

</style>
