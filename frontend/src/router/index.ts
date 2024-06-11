import { createRouter, createWebHistory } from 'vue-router'
import RunView from '../views/RunView.vue'
import ResultView from '../views/ResultView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'easyrun',
      component:RunView
    },{
      path: '/result',
      name: 'resultview',
      component:ResultView
    }
  ]
})

export default router
