import { defineComponent } from "vue";
import "./styles/index.css";
import classes from "@styles/test.modules.css"
import "@styles/test.less";

export default defineComponent({
    setup() {
        return () => {
            return <div class={`root ${classes.modulesClass}`}>Hello Vue3 Jsx</div>
        }
    }
})