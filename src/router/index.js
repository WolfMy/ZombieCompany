import Vue from 'vue'
import VueRouter from 'vue-router'
import BatchQuery from '@/components/BatchQuery.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/SingleQuery',
    name: 'SingleQuery',
    component: () => import('@/components/SingleQuery.vue'),
  },
  {
    path: '/BatchQuery',
    name: 'BatchQuery',
    component: BatchQuery
  },
  {
    path: '/DataVisualization/BasicInformation',
    name: 'BasicInformation',
    component: () => import('@/components/DataVisualization/BasicInformation.vue')
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
    redirect: '/BatchQuery'
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
