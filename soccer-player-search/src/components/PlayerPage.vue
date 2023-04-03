<template>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
  <div class="container">
    <div class="player-card">
      <h1 class="name">{{ playerData.Name }}</h1>
      <ul class="details">
        <li v-for="(value, key) in detailData.data" :key="key">
          <div class="key">{{ key }}:</div>
          <div class="value">{{ value }}</div>
        </li>
      </ul>
      <router-link
        class="back-link"
        :to="{
          name: 'MapPage',
          query: { visualization_data: this.$route.query.visualization_data, scrollY: this.$route.query.scrollY },
        }"
      >
        Back to Map
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PlayerPage",
  props: ['id'],
  data() {
    return {
      playerData: {},
      detailData: {},
    };
  },
  async created() {
    const players = JSON.parse(this.$route.query.visualization_data).players;
    for (var key in players) {
      if (key === 'point0' || key === 'point1') continue;
      this.playerData[key] = players[key][this.id];
    }
    
    try {
      this.detailData = await axios.post('http://127.0.0.1:5000/player', {
        name: this.playerData['Name'],
        age: this.playerData['Age']
      });
    } catch (error) {
      console.error(error);
    }
  },
};
</script>

<style scoped>
body {
  font-family: 'Orbitron', sans-serif;
}

.container {
  margin-top: 2em;
  margin-bottom: 2em;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.player-card {
  background-color: #f5f5f5;
  border-radius: 10px;
  padding: 20px;
  width: 80%;
  max-width: 600px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.name {
  margin-bottom: 1rem;
  font-size: 2rem;
  text-align: center;
}

.details {
  list-style: none;
  margin: 0;
  padding: 0;
}

li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
  text-align: center;
  border-bottom: 1px solid #ccc;
  padding: 0.5rem 0;
}

.key {
  font-weight: bold;
}

.back-link {
  display: block;
  margin-top: 20px;
  text-align: center;
  color: #007bff;
  text-decoration: none;
}

.back-link:hover {
  color: #0056b3;
  text-decoration: underline;
}
</style>