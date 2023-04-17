<!-- src/components/NavigationBar.vue -->
<template>
  <div class="navbar">
    <div class="nav-item nav-item-1">
      <router-link class="nav-link" to="/">Main Page</router-link>
    </div>
    <div class="nav-item nav-item-2">
      <router-link class="nav-link" to="/search1">Ability Graph</router-link>
    </div>
    <div class="nav-item nav-item-3">
      <router-link class="nav-link" to="/search2">Similarity Graph</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavigationBar",
};
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
  z-index: 1000;
}

.nav-item {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: background-color 0.3s, color 0.3s;
}

.nav-item-1,
.nav-item-3 {
  background-color: black;
  color: white;
}

.nav-item-2 {
  background-color: white;
  color: black;
}

.nav-item:hover {
  background-color: white;
  color: black;
}

.nav-item-2:hover {
  background-color: black;
  color: white;
}

.nav-link {
  text-decoration: none;
  color: inherit;
  font-size: 3rem;
}

.nav-link:hover {
  text-decoration: underline;
}
</style>
