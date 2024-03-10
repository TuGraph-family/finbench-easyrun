import { createRouter, createWebHistory } from 'vue-router'
import RunView from '../views/RunView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'easyrun',
      component:RunView
    }
  ]
})

export default router
