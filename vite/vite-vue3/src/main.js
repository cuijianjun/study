import { createApp } from 'vue'
import "./style.css";
import App from "./App";

// import Worker from "./worker?workeer"
// const worker = new Worker();
// worker.onmessage = function (e) {
//     console.log(e);
// }

const globModules = import.meta.glob('./glob')
console.log(globModules);

Object.entries(globModules).forEach(([k,v]) => {
    console.log(k + ":");
    v().then(m => console.log(m.default))
})

createApp(App).mount('#app')
