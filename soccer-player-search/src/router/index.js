import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import MapPage from '../components/MapPage.vue';
import PlayerPage from '../components/PlayerPage.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: "/map/:visualization_data",
    name: "MapPage",
    component: MapPage,
    props: true,
  },
  {
    path: '/player/:name',
    name: 'PlayerPage',
    component: PlayerPage,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
