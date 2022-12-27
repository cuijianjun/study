import './style.css'
import javascriptLogo from './javascript.svg'
import { setupCounter } from './counter.js'

export function render(){
  document.querySelector('#app').innerHTML = `
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
      <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
    </a>
    <h1>Hello Vite!</h1>
    <div class="card">
      <button id="counter" type="button"></button>
    </div>
    <p class="read-the-docs">
      Click on the Vite logo to learn more
    </p>
  </div>
`

setupCounter(document.querySelector('#counter'))
}

render();

if(import.meta.hot) {
  // import.meta.hot.accept();
  import.meta.hot.data.cache = {// 数据还存在 状态还在
    getIndex() {
      return index
    }
  }
  import.meta.hot.invalidate() // 强制浏览器刷新
  import.meta.hot.dispose(() => {// 取消定时器
    if (timer) {clearInterval(timer)}
  })
}
