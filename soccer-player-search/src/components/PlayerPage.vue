<template>
  <link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
  <NavigationBar />
  <div class="container">
    <div class="player-card">
      <h1 class="name">{{ playerData.Name }}</h1>
      <ul class="details">
        <li v-for="(value, key) in filteredDetails" :key="key">
          <div class="key">{{ key }}:</div>
          <div class="value" v-if="key !== 'nei'">{{ value }}</div>
          <div class="value" v-else>
            <template v-if="key === 'nei'">
              <router-link
                v-for="(neighbor, index) in value" :key="index"
                :to="{
                  name: 'PlayerPage',
                  params: { id: neighbor.index },
                  query: { visualization_data: this.$route.query.visualization_data },
                }"
              >
                {{ neighbor.name }}
              </router-link>
            
            </template>
          </div>
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
import NavigationBar from "@/components/NavigationBar.vue";
import axios from "axios";
export default {
  name: "PlayerPage",
  components: {
    NavigationBar,
  },
  props: ['id'],
  data() {
    return {
      playerData: {},
      detailData: {},
    };
  },
  async created(){
      const newId = this.id;
      const players = JSON.parse(this.$route.query.visualization_data).players;
      for (var key in players) {
        if (key === 'point0' || key === 'point1') continue;
        this.playerData[key] = players[key][newId];
      }
      if (players.nei && players.nei[newId]) {
        this.playerData['nei'] = players.nei[newId];
      } else {
        this.playerData['nei'] = [];
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
  watch: {
    async id() {
      const newId = this.id;
      const players = JSON.parse(this.$route.query.visualization_data).players;
      for (var key in players) {
        if (key === 'point0' || key === 'point1') continue;
        this.playerData[key] = players[key][newId];
      }
      if (players.nei && players.nei[newId]) {
        this.playerData['nei'] = players.nei[newId];
      } else {
        this.playerData['nei'] = [];
      }
      try {
        this.detailData = await axios.post('http://127.0.0.1:5000/player', {
          name: this.playerData['Name'],
          age: this.playerData['Age']
        });
      } catch (error) {
        console.error(error);
      }
    }
  },
  computed: {
    filteredDetails() {
      const filtered = {};
      for (const key in this.detailData.data) {
        if (key !== "isAM" && key !== "isD" && key !== "isGK" && key !== "isM" && key !== "isST") {
          filtered[key] = this.detailData.data[key];
        }
      }
      if(this.playerData['nei'].length>0){
        filtered['nei'] = [];
        for (const ind of this.playerData['nei']) {
          filtered['nei'].push({ index: ind, name: JSON.parse(this.$route.query.visualization_data).players['Name'][ind] });
          console.log(JSON.parse(this.$route.query.visualization_data).players['Name'][ind]);
        }
        
      }
      

      return filtered;
    },
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
