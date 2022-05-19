<template>
   <div
      v-for="playlist in playlists"
   >
      <MenuButton
         :menu_name="playlist.title"
         :router_link="playlist.title">
         <img src="../assets/menu/playlist.svg" alt="menu-icon">
      </MenuButton>
   </div>
</template>

<script>
import axios from "axios";
import MenuButton from "@/components/MenuButton";

export default {
   name: "Playlists",
   components: {
      MenuButton
   },
   data() {
      return {
         playlists: []
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
