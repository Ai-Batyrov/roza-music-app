<template>
   <div class="card">
      <div class="card-inner">
         <div class="top">
            <span class="cover"></span>
            <span class="title">{{ title }}</span>
         </div>
         <div class="bottom">
            <span class="create-time">
               {{ create_time }}
            </span>
            <div class="play-div">
               <router-link :to="{ name: 'chart-playlist', params: { id: chart_id } }">
                  <CardButtons name="Play"/>
               </router-link>
            </div>
         </div>
      </div>
   </div>
</template>

<script>
import CardButtons from "@/components/buttons/CardButtons";

export default {
   name: "ChartCard",
   components: {CardButtons},
   data() {
      return {}
   },
   props: {
      title: String,
      create_time: String,
      chart_id: Number
   }
}
</script>

<style scoped lang="less">
@import "@/assets/css/style.less";

.card {
   width: 15rem;
   height: 17rem;
   margin: 0 1rem 0 1rem;
   border-radius: 0.5rem;
   background-color: #436372;
}

.card-inner {
   width: 90%;
   height: 95%;
   .flex-column-direction();
   margin: 0 auto;
   justify-content: space-between;
}

.top {
   width: 100%;
   height: 80%;
   .centering();
   flex-direction: column;
   justify-content: space-around;
   align-items: flex-start;

   .cover {
      width: 100%;
      height: 70%;
      border-radius: 0.5rem;
      background: #E6ECFF;
   }

   .title {
      .global-font();
      font-size: 1rem;
      color: #ffffff;
   }
}

.bottom {
   width: 100%;
   height: 10%;
   .centering();
   justify-content: space-between;

   .create-time {
      .global-font();
      font-size: 0.8rem;
      width: 50%;
      height: 100%;
      .centering();
      justify-content: flex-start;
      color: #bcc1ce;
   }

   .play-div {
      width: auto;
      height: auto;
   }
}

a {
   text-decoration: none;
}
</style>
