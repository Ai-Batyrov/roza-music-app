<template>
   <div class="charts-page">
      <div class="charts-view">
         <div class="headline">
            <h2>Charts</h2>
         </div>
         <div class="charts-list-div">
         <span class="arrow">
            <img :src="arrow_1" alt="arrow-left"/>
         </span>
            <div class="cards-div">
               <div class="card" v-for="chart in charts" v-bind:id="chart.id">
                  <ChartCard
                     :title="chart.title"
                     :create_time="chart.creat_date"
                     :chart_id="chart.id"
                  />
               </div>
            </div>
            <span class="arrow">
            <img :src="arrow_2" alt="arrow-right"/>
         </span>
         </div>
      </div>
      <div class="chart-playlist">
         <router-view></router-view>
      </div>
   </div>
</template>

<script>
import axios from "axios";
import arrow_1 from '../assets/arrows/arrow 1.svg'
import arrow_2 from '../assets/arrows/arrow 2.svg'
import ChartCard from "@/components/charts/ChartCard"

export default {
   name: "ChartsView",
   components: {ChartCard},
   data() {
      return {
         charts: [],
         arrow_1, arrow_2,
      };
   },
   mounted() {
      this.getCharts()
   },
   methods: {
      getCharts() {
         axios
            .get('/api/v1/charts/')
            .then(response => {
               this.charts = response.data
            })
            .catch(error => {
               console.log(error);
            });
      }
   }
}
</script>

<style scoped lang="less">
@import "@/assets/css/style.less";

.charts-page {
   width: 100%;
   height: 100%;
}

.charts-view {
   width: 100%;
   height: 40%;
   display: flex;
   flex-direction: column;
   justify-content: space-between;
   align-items: flex-start;
}

.chart-playlist {
   width: 100%;
   height: 60%;
}

h2 {
   .global-font();
}

.charts-list-div {
   width: 100%;
   height: auto;
   display: flex;
   justify-content: space-between;
   align-items: center;
}

.cards-div {
   display: flex;
   width: 95%;
   justify-content: space-around;
}

.arrow {
   width: 1.5rem;
   height: 3rem;
   .centering();
   border-radius: 0.3rem;
   background-color: #CCEDFF;

   img {
      width: 1.2rem;
   }
}

a {
   text-decoration: none;
}
</style>
