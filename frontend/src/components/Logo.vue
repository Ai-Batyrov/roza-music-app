<template>
   <div class="logo">
      <div class="logo-inner">
         <div>
            <span>
              ROZA
            </span>
         </div>
      </div>
   </div>
</template>

<script>
export default {
   name: "Logo"
}
</script>

<style scoped lang="less">
.centering {
   display: flex;
   justify-content: flex-start;
   align-items: center;
}

.logo {
   width: 100%;
   height: 5rem;
   .centering();
   justify-content: center;
}

.logo-inner {
   width: 90%;
   height: 100%;
   .centering();

   div {
      width: 8rem;
      height: 3.2rem;
      background-color: #7683C8;
      border-radius: 0.5rem;
      display: flex;
      justify-content: center;
      align-items: center;

      span {
         padding: 0;
         margin: 0;
         font-family: Montserrat, sans-serif;
         font-size: 2rem;
         font-weight: 600;
         text-align: center;
         color: #f4f4f4;
         user-select: none;
      }
   }
}

</style>
