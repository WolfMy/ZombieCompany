import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/Home',
    name: Home,
    component: Home
  },
  {
    path: '/BatchQuery',
    name: 'BatchQuery',
    component: () => import ('@/components/BatchQuery.vue')
  },
  {
    path: '/DataVisualization/BasicInformation',
    name: 'BasicInformation',
    component: () => import ('@/components/DataVisualization/BasicInformation.vue')
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
    path: '/DataVisualization/ModelTraining',
    name: 'ModelTraining',
    component: () => import('@/components/DataVisualization/ModelTraining.vue')
  },
  {
    // 默认跳转
    path: '*',
    redirect: '/Home'
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
