<template>
  <div>
    <h1>{{ playerdata.Name }}</h1>
    <ul>
        {% for k in playerdata %}
            <li>{{k}}: {{playerdata[k]}}</li>
        {% endfor %}
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PlayerPage",
  data() {
    return {
      playerdata: {},
    };
  },
  mounted() {
    this.getPlayerData();
  },
  methods: {
    async getPlayerData() {
      const playerName = this.$route.params.name;
      const response = await axios.get(`/player/${playerName}`);
      this.playerdata = response.data;
    },
  },
};
</script>

<style scoped>
h1 {
  margin-bottom: 1rem;
  font-size: 2rem;
}
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
li {
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
}
</style>