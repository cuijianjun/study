const path = require("path");
const fs = require("fs")
let template = fs.readFileSync("index.html", "utf-8");
const render = require("./dist/server/server-entry").render;

const routerToRender = fs.readdirSync("src/pages").map((file) => {
    return file.replace(".jsx", "").toLowerCase();
});

for (const route of routerToRender) {
    const context = {};
    render(route, context).then((html) => {
        const responseHtml = template.replace("<!-- APP_HTML -->", html)
        const filePath = `dist/static/${route}.html`;
        fs.writeFile(filePath, responseHtml);
    });
    
}