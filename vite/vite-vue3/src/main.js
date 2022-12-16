import { createApp } from 'vue'
import "./style.css";
import App from "./App";

import Worker from "./worker?workeer"
const worker = new Worker();
worker.onmessage = function (e) {
    console.log(e);
}
createApp(App).mount('#app')
