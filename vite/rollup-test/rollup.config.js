import json from "@rollup/plugin-json"

export default [
    {
        input: "index.js",
        plugins: [json()],
        output: {
            file: "dist.umd.js",
            format: "umd",
            name: "Index"
        }
    },
    {
        input: "index.js",
        plugins: [json()],
        output: {
            file: "dist.es.js",
            format: "es",
            name: "Index"
        }
    }
]