<!-- static/Header.vue -->
<template>
  <div>
    <div class="header" v-show="showHeader">Soccer Player Search Engine</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showHeader: false
    };
  },
  mounted() {
    setTimeout(() => {
      this.showHeader = true;
    }, 500);
  }
};
</script>

<style>
  body {
    background-image: url(https://example.com/bg.jpg);
    background-size: cover;
  }
  
  .header {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    margin-top: 50px;
    animation: fadeIn 2s ease-in;
    color: white;
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
</style>
