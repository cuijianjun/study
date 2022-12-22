import json from "@rollup/plugin-json"
import resolve from "@rollup/plugin-node-resolve"
import commonjs from "@rollup/plugin-commonjs"
export default [
    {
        input: "index.js",
        external: ['react'],
        plugins: [resolve(),commonjs(), json()],
        output: {
            file: "dist/index.umd.js",
            format: "umd",
            name: "Index"
        }
    },
    {
        input: "index.js",
        plugins: [resolve(),commonjs(),json()],
        output: {
            file: "dist/index.es.js",
            format: "es",
            name: "Index"
        }
    }
]