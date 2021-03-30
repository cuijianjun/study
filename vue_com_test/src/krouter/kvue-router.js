// 实现一个插件
// 返回一个函数
// 或者返回一个对象 他有一个install方法

let _Vue 

class VueRouter {
  constructor(options) {
    this.$options = options
  }
}

VueRouter.install = function (Vue) {
  // 引用Vue构造函数，在上边VueRouter中使用
  _Vue = Vue
  Vue.mixin({
    beforeCreate() {
      Vue.prototype.$router = this.$options.router
    },
  })
  
}

export default VueRouter