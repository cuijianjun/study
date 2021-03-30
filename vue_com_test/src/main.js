import Vue from 'vue'
import App from './App.vue'
// import router from './router'
import router from './krouter'
import store from './kstore'


Vue.config.productionTip = false

new Vue({
  store,
  router, // 让vue在插件中，可以获取到vue的实例
  render: h => h(App),
}).$mount('#app')
