import Notice from './Notice'
function createNotice ({ Vue, title, message, propsData, onClose }) {
  const Constructor = Vue.extend(Notice)
  const n = new Constructor({ propsData: { title, message } })
  n.$mount()
  document.body.appendChild(n.$el)
}

export default {
  install (Vue) {
    Vue.prototype.$notice = function (title, message, option) {
      createNotice({
        Vue,
        title,
        message,
        propsData: option,
        onclose: () => {}
      })
    }
  }
}