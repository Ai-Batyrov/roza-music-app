<template>
   <div class="menu-item">
      <router-link :to="router_link">
         <div class="icon-div">
            <span class="menu-item-icon">
               <img :src="iconUrl" alt="menu-icon-url">
            </span>
         </div>
         <div class="menu-name">
            <span>
             {{ menu_name }}
            </span>
         </div>
      </router-link>
   </div>
</template>

<script>
export default {
   name: "MenuButton",
   props: {
      menu_name: String,
      router_link: String,
      iconUrl: String
   }
}
</script>

<style scoped lang="less">
@import "@/assets/css/style.less";

a {
   width: 100%;
   height: 100%;
   text-decoration: none;
   .centering();
   color: #000000;
   border-radius: 0.5rem;
   transition: all 0.3s ease-in-out;
}

a:hover {
   background-color: #E6ECFF;
}

.router-link-active {
   background-color: #16659D;

   .menu-item-icon > img {
      filter: invert(1);
   }

   .menu-name {
      color: #ffffff;
   }
}

.router-link-active:hover {
   background-color: #1c89d1;
}


.menu-item {
   width: 15rem;
   height: 3rem;
   margin: 0.3rem 0 0.3rem 0;
   user-select: none;
}

.icon-div {
   width: 3rem;
   height: 3rem;
   .centering();
}

.menu-name {
   width: 80%;
   height: 100%;

   span {
      width: 90%;
      height: 100%;
      display: flex;
      align-items: center;
      font-family: Poppins, sans-serif;
      font-size: 1rem;
      text-decoration: none;
   }
}
</style>
