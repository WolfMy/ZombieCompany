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

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
