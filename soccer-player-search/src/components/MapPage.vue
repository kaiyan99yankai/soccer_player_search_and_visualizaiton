<template>
<link href="https://fonts.googleapis.com/css2?family=Orbitron&display=swap" rel="stylesheet">
  <div>
    <canvas
      ref="canvas"
      @click="handleClick"
      @mousemove="handleMouseMove"
    ></canvas>
    <div
      v-if="hoveredPlayer"
      class="tooltip"
      :style="{ top: tooltipY + 'px', left: tooltipX + 'px' }"
    >
      {{ players.Name[hoveredPlayer] }}
    </div>
  </div>
</template>

<script>
export default {
  name: "MapCanvas",
  props: ["visualization_data", "scrollY"],
  data() {
    return {
      width: 0,
      height: 0,
      players: {},
      ctx: null,
      hoveredPlayer: null,
      tooltipX: 0,
      tooltipY: 0,
    };
  },
  created() {
    const parsedData = JSON.parse(this.visualization_data);
    this.width = parsedData.canvas_width;
    this.height = parsedData.canvas_height;
    this.players = parsedData.players;
  },
  mounted() {
    this.$refs.canvas.width = this.width;
    this.$refs.canvas.height = this.height;
    this.ctx = this.$refs.canvas.getContext("2d");
    this.drawPlayers();
    if (this.scrollY) {
      window.scrollTo(0, this.scrollY);
    }else{
      window.scrollTo(0, 0);
    }
  },

  methods: {
    drawPlayers() {
      for (const key in this.players.Name) {
        const x = this.players.point0[key];
        const y = this.players.point1[key];
        this.drawPlayer(x, y);
      }
    },
    drawPlayer(x, y, color = "grey") {
      this.ctx.beginPath();
      this.ctx.arc(x, y, 5, 0, Math.PI * 2);
      this.ctx.fillStyle = color;
      this.ctx.fill();
      this.ctx.closePath();
    },
    handleClick() {
      if (this.hoveredPlayer) {
        const playerId = this.hoveredPlayer;
        const scrollY = window.scrollY;
        this.$router.push({
          name: "PlayerPage",
          params: { id: playerId },
          query: { visualization_data: this.visualization_data, scrollY: scrollY,},
        });
      }
    },
    handleMouseMove(event) {
      const rect = this.$refs.canvas.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;

      let foundPlayer = false;
      for (const key in this.players.Name) {
        const playerX = this.players.point0[key];
        const playerY = this.players.point1[key];
        const distance = Math.sqrt(
          Math.pow(x - playerX, 2) + Math.pow(y - playerY, 2)
        );

        if (distance <= 5) {
          foundPlayer = true;
          if (this.hoveredPlayer !== key) {
            if (this.hoveredPlayer) {
              const prevX = this.players.point0[this.hoveredPlayer];
              const prevY = this.players.point1[this.hoveredPlayer];
              this.drawPlayer(prevX, prevY);
            }
            this.hoveredPlayer = key;
            this.drawPlayer(playerX, playerY, "red");
            this.tooltipX = event.pageX + 10;
            this.tooltipY = event.pageY + 10;
          }
          break;
        }
      }

      if (!foundPlayer && this.hoveredPlayer) {
        const prevX = this.players.point0[this.hoveredPlayer];
        const prevY = this.players.point1[this.hoveredPlayer];
        this.drawPlayer(prevX, prevY);
        this.hoveredPlayer = null;
      }
    },
  },
};
</script>

<style scoped>
.tooltip {
  font-family: 'Orbitron', sans-serif;
  position: absolute;
  background-color: rgba(0,0, 0, 0.7);
  color: white;
  border-radius: 5px;
  padding: 5px;
  z-index: 100;
  }
</style>
