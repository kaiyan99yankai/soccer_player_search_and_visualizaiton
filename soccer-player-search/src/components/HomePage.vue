<template>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet" />
  <div>
    <parallax-background :scroll-y="scrollY"></parallax-background>
    <div class="home-page">
      <div class="header">
      </div>
      <div class="sections-container">
        <section v-for="(section, index) in sections" :key="index" :class="{ 'white-background': index === 0, 'grey-background': index === 1 }" class="section">
          <div class="image-container">
            <router-link :to="section.link">
              <div class="section-image">
                <img
                  :src="require(`./${section.image}`)"
                  alt="Section Image"
                  class="image"
                  @mouseover="enlargeImage"
                  @mouseout="resetImage"
                />
              </div>
            </router-link>
          </div>
          <div class="section-text">
            <h2>{{ section.title }}</h2>
            <p>{{ section.description }}</p>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import ParallaxBackground from './ParallaxBackground.vue'

export default {
  name: "HomePage",
  components: {
    ParallaxBackground,
  },
  data() {
    return {
      sections: [
        {
          title: "Ability Node Graph",
          description: "Use dimension reduction method to show the selected player in 2D graph given by their ability.",
          image: 'images.jpeg',
          link: { name: "Search1" },
        },
        {
          title: "Similarity Node Graph",
          description: "Use link between player nodes to show the similarity between them",
          image: "graph.png",
          link: { name: "Search2" },
        },
      ],
      scrollY: 0,
    };
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
    enlargeImage(event) {
      event.target.style.transform = "scale(1.1)";
    },
    resetImage(event) {
      event.target.style.transform = "scale(1)";
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
  font-family: "Orbitron", sans-serif;
}

.title {
  font-size: 3rem;
  color: #333;
}

.sections-container {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
}

.section {
  display: flex;
  align-items: center;
  gap: 3rem;
  justify-content: center;
}

.section-image {
  margin: auto;
  width: 50%;
  height: auto;
  cursor: pointer;
  transition: transform 0.5s ease-out;
}

.image-container{
  width: 50%;
  height: auto;
}


.section-text {
  width: 50%;
  display: flex;
  flex-direction: column;
  gap: 5rem;
  font-size: 1.5rem;
}

.white-background {
  background-color: white;
}

.grey-background {
  background-color: #f2f2f2;
}

.image {
  width: 100%;
}

.enlarged-image {
  transform: scale(1.1);
}

@media screen and (max-width: 768px) {
  .section {
    flex-direction: column;
    align-items: center;
  }

  .section-image {
    width: 80%;
  }

  .section-text {
    width: 80%;
    margin-top: 1rem;
  }
}

</style>