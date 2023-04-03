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
    path: "/map",
    name: "MapPage",
    component: MapPage,
    props: route => {
      const props = { visualization_data: route.query.visualization_data };
      if (route.query.scrollY) {
        props.scrollY = Number(route.query.scrollY);
      }
      return props;
    },
  },
  {
    path: '/players/:id',
    name: 'PlayerPage',
    component: PlayerPage,
    props: route => {
      const params = {
        id: route.params.id,
        visualization_data: route.query.visualization_data,
      };
      return params;
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
