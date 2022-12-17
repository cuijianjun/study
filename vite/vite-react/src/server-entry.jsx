import ReactDOMServer from "react-dom/server";
import { StaticRouter } from "react-routeer-dom";
import { App } from "./App";

export function render(url, context){
    return ReactDOMServer.renderToString(
        <StaticRouter location={url} context={context}>
            <App/>
        </StaticRouter>
    )
}