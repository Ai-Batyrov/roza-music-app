<template>
   <div class="menu-group">
      <div class="group-name">
         <h2>
            {{ group_name }}
         </h2>
      </div>
      <div class="items">
         <slot></slot>
      </div>
   </div>
</template>

<script>
export default {
   name: "MenuGroup",
   props: {
      group_name: String
   }
}
</script>

<style scoped lang="less">
@import "@/assets/css/style.less";

.menu-group {
   width: 100%;
   height: auto;
   display: flex;
   flex-direction: column;
   align-items: flex-end;
   margin-bottom: 0.8rem;
}

.group-name {
   width: 100%;
   height: 2rem;
   margin: 0.3rem 0 0.3rem 0;
   .centering();

   h2 {
      width: 90%;
      font-family: Poppins, sans-serif;
      font-weight: 500;
      font-size: 1rem;
      opacity: 0.5;
      margin: 0;
      padding: 0;
   }
}

.items {
   width: 90%;
   height: auto;
   display: flex;
   flex-direction: column;
}
</style>
