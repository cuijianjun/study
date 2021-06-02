// import HelloWorld from '@/components/HelloWorld.vue'
import { createApp, defineComponent, h } from 'vue'
import App from './App.vue'

// const App = defineComponent({
//   render() {
//     return h(
//       'div',
//       {
//         id: 'app',
//       },
//       [
//         h('img', {
//           alt: 'Vue logo',
//           src: '',
//         }),
//         h(HelloWorld, {
//           msg: 'Welcome to ypur Vue.js + ts',
//         }),
//       ],
//     )
//   },
// })

createApp(App).mount('#app')
