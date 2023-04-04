
<template>
<link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
  <div>
    <parallax-background :scroll-y="scrollY"></parallax-background>
    <div class="home-page">
      <div class="header">
        <h1 class="title animated fadeInDown">
          Soccer Player Search Engine
        </h1>
      </div>
      <div class="search-container">
        <div
          class="login-box"
          :style="{ top: `${top}px`, left: `${left}px`, position: position }"
        >
          <form @submit.prevent="submitForm">
            <div class="user-box">
              <input type="number" id="bottom" v-model.number="bottom" required />
              <label>Bottom</label>
            </div>
            <div class="user-box">
              <input type="number" id="top" v-model.number="top" required />
              <label>Top</label>
            </div>
            <div class="user-box">
              <input v-model="position" required />
              <label>Position</label>
            </div>
            <button type="submit">
              <span></span>
              <span></span>
              <span></span>
              <span></span>
              Search
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ParallaxBackground from './ParallaxBackground.vue'
export default {
  name: "HomePage",
  components: {
    ParallaxBackground,
  },
  data() {
    return {
      bottom: "",
      top: "",
      position: "",
      scrollY: 0,
    }
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post('/', {
          bottom: this.bottom,
          top: this.top,
          position: this.position,
      });
        let visualization_data = JSON.stringify(response.data)
        this.$router.push({
          name: 'MapPage',
          query: {visualization_data: visualization_data}
        });
      } catch (error) {
        console.error(error);
      }
      
    },
    onScroll() {
      this.scrollY = window.scrollY;
    },
  },
  
};
</script>

<style scoped>
    .home-page {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    
    .header {
      margin-bottom: 2rem;
      font-family: 'Orbitron', sans-serif;
    }
    
    .title {
      font-size: 3rem;
      color: #333;
    }
    

    @media screen and (max-width: 768px) {
        .form-container {
            width: 100%;
        }
    }
    </style>
