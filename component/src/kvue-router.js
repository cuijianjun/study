let Vue;
class KVueRouter {
  constructor(options) {
    this.$options = options;
    this.routeMap = {}
    
    this.app = new Vue({
      data: {
        current: '/'
      }
    })
  }
  
  init() {
    this.bindEvents();
    this.createRouteMap();
    this.initComponent();
  }
  
  bindEvent() {
    window.addEventListener('hashchange', this.onHashChange.bind(this))
  }
  
  onHashChange() {
    this.app.current = window.location.hash.slice(1) || '/';
  }
  
  createRouteMap() {
    this.$options.routes.forEach(route => {
      this.routeMap[route.pash] = route;
    })
  }
  
  initComponent() {
    Vue.component('router-link', {
      props: {
        to: String
      },
      render(h) {
        return (<a href={"#" + this.to}>{this.$slots.default}</a>);
      }
    })
    Vue.component('router-view', {
      render: (h) => {
        const Component = this.routeMap[this.app.current].component;
        return h(Component)
      }
    })
  }
}

KVueRouter.install = function (_Vue) {
  Vue = _Vue;
  Vue.mixin({
    beforeCreate() {
      if (this.$options.router) {
        Vue.prototype.$router = this.$options.router;
      }
    }
  })
}

export default KVueRouter