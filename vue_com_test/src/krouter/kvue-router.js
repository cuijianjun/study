// 实现一个插件
// 返回一个函数
// 或者返回一个对象 他有一个install方法

let _Vue 

class VueRouter {
  constructor(options) {
    this.$options = options

    // 缓存path和route的映射关系
    this.routeMap = {}
    this.$options.routes.forEach(
      route => {
        this.routeMap[route.path] = route
      }
    )
    // 需要定义一个响应式的current属性
    const initial = window.location.hash.slice(1) || '/'
    _Vue.util.defineReactive(this, 'current', initial)

    // 监控url变化
    window.addEventListener('hashchange', this.onHashChange.bind(this))
  }

  onHashChange() {
    // 只要#后面的部分
    this.current = window.location.hash.slice(1)
  }
  
  
}

VueRouter.install = function (Vue) {
  // 引用Vue构造函数，在上边VueRouter中使用
  _Vue = Vue
  Vue.mixin({
    beforeCreate() {
      if (this.$options.router) {
        Vue.prototype.$router = this.$options.router
      }
    },
  })
  
  // 定义两个全局的组件 router-link ，router-view
  Vue.component('router-link', {
    props: {
      to: {
        type: String,
        require: true
      }
    },
    render(h) {
      // <a>XXX</a>
      return h('a', {
        attrs: {
          href: '#' + this.to,
        }
      }, this.$slots.default)
    }
  })
  Vue.component('router-view', {
    render(h){
      let component = null;
      // 找到当前url对应的组件
      // const route = this.$router.$options.routes.find(route => route.path === this.$router.current)
      // if (route) {
      //   component = route.component
      // }
      const {routeMap, current} = this.$router
      component = routeMap[current]? routeMap[current].component: null
      // 渲染传入组件
      return h(component)
    }
  })
  
}

export default VueRouter