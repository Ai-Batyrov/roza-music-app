<template>
   <div>
      <div class="sidebar">
         <logo/>
         <div class="sidebar-menu">
            <MenuGroup group_name="Services">
               <MenuButton menu_name="Charts" router_link="/">
                  <img src="./assets/menu/charts.svg" alt="menu-icon">
               </MenuButton>
               <MenuButton menu_name="Radio Stations" router_link="/radio">
                  <img src="./assets/menu/radio.svg" alt="menu-icon"/>
               </MenuButton>
               <MenuButton menu_name="Search" router_link="/search">
                  <img src="./assets/menu/search.svg" alt="menu-icon"/>
               </MenuButton>
            </MenuGroup>

            <MenuGroup group_name="My Music">
               <MenuButton menu_name="Liked Songs" router_link="/liked">
                  <img src="./assets/menu/like.svg" alt="menu-icon">
               </MenuButton>
               <MenuButton menu_name="Albums" router_link="/albums">
                  <img src="./assets/menu/album.svg" alt="menu-icon"/>
               </MenuButton>
            </MenuGroup>

            <MenuGroup group_name="Playlists">
               <Playlists/>
            </MenuGroup>
         </div>
         <copyright/>
      </div>
      <div class="main">
         <router-view/>
      </div>
      <div class="sidebar">

      </div>
   </div>
</template>

<style lang="less">
body, html {
   width: 100vw;
   height: 100vh;
   overflow: hidden;
   margin: 0;
   padding: 0;
}

#app {
   width: 100%;
   height: 100%;
   margin: 0;
   padding: 0;

   div {
      display: flex;
   }
}

.sidebar {
   width: 20%;
   height: 100vh;
   display: flex;
   flex-direction: column;
}

.main {
   width: 60%;
   height: 100%;
}

.sidebar-menu {
   width: 100%;
   height: 90%;
   display: flex;
   flex-direction: column;
}
</style>
<script>
import Logo from "@/components/Logo";
import Copyright from "@/components/Copyright";
import MenuButton from "@/components/MenuButton";
import MenuGroup from "@/components/MenuGroup";
import axios from "axios";
import Playlists from "@/components/Playlists";

export default {
   components: {Playlists, MenuGroup, MenuButton, Copyright, Logo}
}
</script>
