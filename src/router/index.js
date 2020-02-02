import Vue from 'vue'
import VueRouter from 'vue-router'
import BatchQuery from '@/components/BatchQuery.vue'
import DataVisualization from '@/components/Echarts.vue'
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
    path: '/DataVisualization',
    name: 'DataVisualization',
    component: DataVisualization
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
