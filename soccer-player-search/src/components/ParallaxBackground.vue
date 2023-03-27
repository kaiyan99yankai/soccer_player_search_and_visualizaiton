<template>
<link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
  <div class="parallax-container">
    <div class="parallax-layer layer1">
      <span class="scroll-text">Scroll down to search for players</span>
    </div>
    <div class="parallax-layer layer2"></div>
  </div>
</template>

<script>
export default {
  name: 'ParallaxBackground',
  methods: {
    onScroll() {
        const scrollTop = window.scrollY;
        const maxOpacity = 1;
        const minOpacity = 0;
        const fadeDistance = 300; // 淡出距离，可根据需要调整

        const opacity = Math.max(minOpacity, maxOpacity - scrollTop / fadeDistance);

        const textElement = this.$el.querySelector(".scroll-text");
        if (textElement) {
            textElement.style.opacity = opacity;
        }
    },
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.onScroll);
  },
}
</script>

<style scoped>
.parallax-container {
  position: relative;
  overflow: hidden;
  height: 100vh;
}

.parallax-layer {
  position: absolute;
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

.layer1 {
  background-image: url('../assets/bg1.png');
  background-attachment: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
}

.layer2 {
  background-attachment: fixed;
  transform: translateY(50%);
}

.scroll-text {
font-family: 'Orbitron', sans-serif;
  font-size: 80px;
  text-align: center;
  color: #fff;
  animation: glow 2s ease-in-out infinite alternate;
  opacity: 1;
}

@keyframes glow {
  from {
    text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #fff;
  }
  to {
    text-shadow: 0 0 20px #fff, 0 0 30px #fff, 0 0 40px #fff, 0 0 50px #fff;
  }
}

</style>