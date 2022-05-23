<template>
   <div>
      <div class="sidebar">
         <logo/>
         <div class="sidebar-menu">
            <MenuGroup group_name="Services">
               <MenuButton menu_name="Charts" router_link="/" :icon-url="chartIconUrl"
               >
               </MenuButton>
               <MenuButton menu_name="Radio Stations" router_link="/radio" :icon-url="radioIconUrl">
               </MenuButton>
               <MenuButton menu_name="Search" router_link="/search" :icon-url="searchIconUrl">
               </MenuButton>
            </MenuGroup>

            <MenuGroup group_name="My Music">
               <MenuButton menu_name="Liked Songs" router_link="/liked" :icon-url="likeIconUrl">
               </MenuButton>
               <!--               <MenuButton menu_name="Albums" router_link="/albums" :icon-url="albumsIconUrl">-->
               <!--               </MenuButton>-->
            </MenuGroup>

            <MenuGroup group_name="Playlists">
               <Playlists/>
            </MenuGroup>
         </div>
         <copyright/>
      </div>
      <div class="main">
         <transition
            enter-active-class="animated pulse"
            leave-active-class="animated pulse"
            name="router-anim"
         >
            <router-view/>
         </transition>
      </div>
      <div class="sidebar">
         <div class="controls">
            <div class="controls-inner">
               <!--               <Controller :icon-url="notificationsIcon"/>-->
               <a href="http://127.0.0.1:8000/upload/">
                  <UploadBtn/>
               </a>

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
@import "https://cdn.jsdelivr.net/npm/animate.css@3.5.1";

body, html {
   width: 100vw;
   height: 100vh;
   //overflow: hidden;
   margin: 0;
   padding: 0;
}

#app {
   width: 100%;
   height: 100%;
   margin: 0;
   padding: 0;
   overflow: hidden;


   div {
      display: flex;
   }
}

.page {
   position: fixed;
   width: inherit;
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

a {
   text-decoration: none;
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
import uploadBtnIcon from "@/assets/uploadTrack.svg"
import chartIconUrl from "@/assets/menu/charts.svg"
import radioIconUrl from "@/assets/menu/radio.svg"
import searchIconUrl from "@/assets/menu/search.svg"
import likeIconUrl from "@/assets/menu/like.svg"
import albumsIconUrl from "@/assets/menu/album.svg"
import Player from "@/components/player/Player";
import UploadBtn from "@/components/buttons/uploadBtn";
import store from "@/store";

export default {
   components: {UploadBtn, Player, UserControl, Playlists, MenuGroup, MenuButton, Copyright, Logo, Controller},
   data() {
      return {
         settingsIcon, notificationsIcon, uploadBtnIcon,
         chartIconUrl, radioIconUrl, searchIconUrl, likeIconUrl, albumsIconUrl
      }
   },
   async mounted() {
      store.dispatch('userLogin', {})
   }
}
</script>
