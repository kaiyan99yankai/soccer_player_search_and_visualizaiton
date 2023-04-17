import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import MapPage from '../components/MapPage.vue';
import PlayerPage from '../components/PlayerPage.vue';
import Search1 from '../components/Search1.vue';
import Search2 from '../components/Search2.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: "/search1",
    name: "Search1",
    component: Search1,
    props: route => {
      const props = {};
      if (route.query.scrollY) {
        props.scrollY = Number(route.query.scrollY);
      }
      return props;
    },
  },
  {
    path: "/search2",
    name: "Search2",
    component: Search2,
    props: route => {
      const props = {};
      if (route.query.scrollY) {
        props.scrollY = Number(route.query.scrollY);
      }
      return props;
    },
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
