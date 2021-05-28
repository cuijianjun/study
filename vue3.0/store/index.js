import {createStore} from "vuex"

export default createStore({
  state: {name: 'dell'},
  mutations: {
    change(state, str) {
      state.name = str
    }
  },
  actions: {
    change(store, str) {
      setTimeout(() => {
        store.commit("change", str)
      }, 2000)
    }
  }
})