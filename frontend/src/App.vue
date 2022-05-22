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
         <router-view></router-view>
      </div>
      <div class="sidebar">
         <div class="controls">
            <div class="controls-inner">
               <Controller :icon-url="notificationsIcon"/>
               <Controller :icon-url="settingsIcon"/>
               <UserControl/>
            </div>
         </div>
         <div class="unknown-div"></div>
         <div class="player-div">
            <Player/>
         </div>
      </div>
   </div>
</template>

<style lang="less">
@import "@/assets/css/style.less";

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

.controls {
   width: 100%;
   height: 5rem;
   .centering();
}

.controls-inner {
   width: 90%;
   height: 70%;
   display: flex;
   justify-content: flex-end;
}

.unknown-div {
   width: 100%;
   height: 37%;
}

.player-div {
   width: 100%;
   height: 60%;
   .centering();
}
</style>
<script>
import Logo from "@/components/Logo";
import Copyright from "@/components/Copyright";
import MenuButton from "@/components/MenuButton";
import MenuGroup from "@/components/MenuGroup";
import Controller from "@/components/controls/Control";
import Playlists from "@/components/Playlists";
import UserControl from "@/components/controls/UserControl";
import settingsIcon from "@/assets/controls/settings.svg"
import notificationsIcon from "@/assets/controls/notifications.svg"
import Player from "@/components/player/Player";

export default {
   components: {Player, UserControl, Playlists, MenuGroup, MenuButton, Copyright, Logo, Controller},
   data() {
      return {
         settingsIcon, notificationsIcon
      }
   }
}
</script>
