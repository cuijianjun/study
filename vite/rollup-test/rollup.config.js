import json from "@rollup/plugin-json"
import resolve from "@rollup/plugin-node-resolve"
import commonjs from "@rollup/plugin-commonjs"
import { terser } from "rollup-plugin-terser"
import ts from "@rollup/plugin-typescript"

export default [
    {
        input: "index.js",
        external: ['react'],
        plugins: [
            resolve(),
            commonjs(),
            ts(),
             json()
            ],
        output: {
             file: "dist/index.umd.js",
            format: "umd",
            name: "Index",
            plugins: [terser()],
        }
    },
    {
        input: "index.js",
        plugins: [resolve(),commonjs(),json()],
        output: {
            file: "dist/index.es.js",
            format: "es",
            name: "Index",
            banner: "/** Hello this is Banner**/"
        }
    }
]