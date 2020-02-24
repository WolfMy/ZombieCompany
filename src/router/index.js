import Vue from 'vue'
import VueRouter from 'vue-router'
import BasicInformation from '@/components/DataVisualization/BasicInformation.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/BatchQuery',
    name: 'BatchQuery',
    component: () => import ('@/components/BatchQuery.vue')
  },
  {
    path: '/DataVisualization/BasicInformation',
    name: 'BasicInformation',
    component: BasicInformation
  },
  {
    path: '/DataVisualization/RelevanceExplore',
    name: 'RelevanceExplore',
    component: () => import('@/components/DataVisualization/RelevanceExplore.vue')
  },
  {
    path: '/DataVisualization/CorporatePortraits',
    name: 'CorporatePortraits',
    component: () => import('@/components/DataVisualization/CorporatePortraits.vue')
  },
  {
    // 默认跳转
    path: '*',
    redirect: '/DataVisualization/BasicInformation'
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
