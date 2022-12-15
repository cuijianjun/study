import { defineComponent } from "vue";
import "./styles/index.css";
import classes from "@styles/test.modules.css"
import "@styles/test.less";
import { a } from "./test"

export default defineComponent({
    setup() {
        return () => {
            return <div class={`root ${classes.modulesClass}`}>Hello {a.name}</div>
        }
    }
})