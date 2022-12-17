const express = require('express');
const { createServer } = require('vite');
const fs = require("fs");
const app = express();

const {createServer: createViteServer} = require("vite");

createViteServer(
    {
        server: {
            middlewareMode: "html",
        }
    }
).then((vite) => {
    app.use(vite.middlewares);

    app.get("*", async (req, res) => {
        
        let template = fs.readFileSync("index.html", "utf-8");
        template = vite.transformIndexHtml(req.url, template);
        const render  = await vite.ssrLoadModule("/src/server-entry.jsx");
        const html = await render(req.url);
        const responseHtml = template.replace("<!-- APP_HTML -->", html);
        res.set("content-type", "text/html").send(responseHtml);
    })
    app.listen(4000);
})