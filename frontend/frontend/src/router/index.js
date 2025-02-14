import { createRouter, createWebHistory } from 'vue-router'
import Shark from '@/pages/Shark.vue'
import Default from '@/pages/Default.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Default',
      component: Default
    },
    {
      path: '/shark',
      name: 'Shark',
      component: Shark
    }
  ],
})

export default router
