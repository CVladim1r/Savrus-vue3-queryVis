import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Dashboard from './views/Dashboard.vue';
import Logs from './views/Logs.vue'


const routes: Array<RouteRecordRaw> = [
  { path: '/', component: Dashboard },
  //{ path: '/settings', component: Settings },
  { path: '/logs', component: Logs }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
