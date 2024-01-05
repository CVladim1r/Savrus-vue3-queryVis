import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Home from './views/Dashboard.vue';


const routes: Array<RouteRecordRaw> = [
  { path: '/', component: Home },
  //{ path: '/settings', component: Settings },
  //{ path: '/logs', component: Logs }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
