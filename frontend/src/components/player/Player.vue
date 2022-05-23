<template>
   <div class="player">
      <div class="inner">
         <div class="top">
            <div class="cover">
               <img :src="current.cover" alt="audio-cover"/>
            </div>
            <div class="info">
               <p class="title">{{ current.title }}</p>
               <p class="artist-name">{{ current.artist }}</p>
            </div>
         </div>
         <div class="bottom">
            <div class="play-control-btn">
               <PlayerPrevButton @click="prev"/>
               <PlayerPlayButton v-if="!isPlaying" @click="play"/>
               <PlayerPauseButton v-else @click="pause"/>
               <PlayerNextButton @click="next"/>
            </div>
         </div>
      </div>
   </div>
</template>

<script src="@/assets/js/Player.js">
</script>

<style lang="less" scoped>
@import "@/assets/css/style.less";

.player {
   width: 17rem;
   height: 23rem;
   border-radius: 1rem;
   background-color: #166ba3;
   .flex-column-direction();
   justify-content: center;
   align-items: center;
}

.inner {
   width: 93%;
   height: 95%;
   .centering();
   flex-direction: column;
}

.top {
   width: 100%;
   height: 85%;
   .flex-column-direction();
   align-items: center;
}

.bottom {
   width: 100%;
   height: 15%;
   .centering();
}

.cover {
   width: 100%;
   height: 80%;
   background-color: #b8d2e5;
   border-radius: 0.5rem;


   img {
      width: 100%;
      height: 100%;
      border-radius: 0.5rem;
   }
}

.info {
   width: 95%;
   height: 20%;
   .flex-column-direction();
   align-items: center;
   justify-content: space-around;

   p {
      margin: 0;
      .global-font();
      color: #ffffff;
   }

   .artist-name {
      opacity: 0.8;
      font-size: 0.9rem;
   }
}

.play-control-btn {
   width: 60%;
   height: 100%;
   display: flex;
   justify-content: space-between;
   align-items: center;
}
</style>
