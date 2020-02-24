import Vue from 'vue'
import App from './App.vue'
import ViewUI from 'view-design'
import 'view-design/dist/styles/iview.css'
import router from '@/router'

Vue.config.productionTip = false
Vue.use(ViewUI)

// 引入echarts
import echarts from 'echarts'
Vue.prototype.$echarts = echarts

//Vue.prototype.$api_baseUrl = 'http://127.0.0.1:5000/'
Vue.prototype.$api_baseUrl = 'http://120.27.192.52:8081/'

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
