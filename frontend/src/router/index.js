import { createRouter, createWebHistory } from 'vue-router'
import Query from '../components/Query.vue';

const routes = [
  // {
  //   path: '/',
  //   name: 'Query',
  //   component: Query
  // },
  {
    path: '/query',
    name: 'Query',
    component: Query
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
