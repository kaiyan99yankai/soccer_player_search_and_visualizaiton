<template>
  <div ref="tooltip" class="tooltip" v-if="showTooltip" :style="{ top: tooltipY + 'px', left: tooltipX + 'px' }">{{ tooltipContent }}</div>
  <div class="map-container">
    <div>
      <p v-if="loading">Loading...</p>
      <div v-else :style="{ margin: 'auto', width: `${width}px`, height: `${height}px` }">
        <a
          v-for="(name, key) in players.Name"
          :key="key"
          :style="{
            position: 'absolute',
            top: players.point1[key] + 'px',
            left: players.point0[key] + 'px',
            backgroundColor: 'blue',
            width: '10px',
            height: '10px',
            borderRadius: '50%',
          }"
          class="glowing"
          @mouseover="showPlayerTooltip($event, name)"
          @mouseout="hidePlayerTooltip"
        ></a>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'MapPage',
  props: ['visualization_data'],
  data () {
    return {
      loading: false,
      width: 0,
      height: 0,
      players: {},
      showTooltip: false,
      tooltipX: 0,
      tooltipY: 0,
      tooltipContent: '',
    }
  },
  created() {
    const parsedData = JSON.parse(this.visualization_data);
    this.width = parsedData.canvas_width;
    this.height = parsedData.canvas_height;
    this.players = parsedData.players;
    for(var player in this.players){
      console.log(player)
    }
  },
  methods: {
    // getPlayerLink (player) {
    //   return `/players/${player.Name}`
    // }
    showPlayerTooltip(event, name) {
      this.showTooltip = true;
      this.tooltipX = event.pageX + 10;
      this.tooltipY = event.pageY + 10;
      this.tooltipContent = name;
    },
    layerTooltip() {
      this.showTooltip = false;
    },
  }
}
</script>

<style scoped>
  .map-container {
    background-color: white;
  }

  .tooltip {
    position: absolute;
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    border-radius: 5px;
    padding: 5px;
    z-index: 100;
  }

  @keyframes glowing {
    0% {
      box-shadow: 0 0 5px #0000ff, 0 0 10px #0000ff, 0 0 20px #0000ff, 0 0 30px #0000ff;
    }
    50% {
      box-shadow: 0 0 10px #0000ff, 0 0 20px #0000ff, 0 0 30px #0000ff, 0 0 40px #0000ff;
    }
    100% {
      box-shadow: 0 0 5px #0000ff, 0 0 10px #0000ff, 0 0 20px #0000ff, 0 0 30px #0000ff;
    }
  }

  .glowing {
    animation: glowing 2s infinite;
    display: block;
  }
</style>