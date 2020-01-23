import Vue from 'vue'
import VueRouter from 'vue-router'
import SingleQuery from '@/components/SingleQuery.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/SingleQuery',
    name: 'SingleQuery',
    component: SingleQuery
  },
  {
    path: '/BatchQuery',
    name: 'BatchQuery',
    component: () => import('@/components/BatchQuery.vue'),
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
