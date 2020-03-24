import Vue from 'vue'
import App from './App.vue'
import ViewUI from 'view-design'
import 'view-design/dist/styles/iview.css'
import router from '@/router'
import axios from 'axios'
import './plugins/element.js'
import 'element-ui/lib/theme-chalk/index.css';

Vue.config.productionTip = false
Vue.use(ViewUI)

// 引入echarts
import echarts from 'echarts'
Vue.prototype.$echarts = echarts

axios.defaults.baseURL = process.env.VUE_APP_API_URL
axios.defaults.timeout = 5000

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
