import { createApp } from 'vue'
import App from './App.vue'
import './assets/formStyles.css'
import router from "./router/index.js"; // 导入路由

import { VTooltip } from 'v-tooltip';

const app = createApp(App);
app.directive('tooltip', VTooltip);
app.use(router);
app.mount('#app');
