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
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
