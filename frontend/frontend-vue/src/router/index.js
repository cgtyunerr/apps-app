import { createRouter, createWebHistory } from 'vue-router'
import AssetView from '../views/AssetView.vue'
import CampaignView from '../views/CampaignView.vue'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/asset',
      name: 'asset',
      component: AssetView,
    },
    {
      path: '/campaign',
      name: 'campaign',
      component: CampaignView,
    },
  ],
})

export default router
