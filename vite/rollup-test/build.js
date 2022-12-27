let exampleOnloadPlugin = {
    name: 'example',
    setup(build) {
        let fs = require('fs');

        build.onResolve({filter: /\.txt$/}, async (args) => ({
            path: args.path,
            namespace: 'txt'
        }));
        
        build.onLoad({filter: /\.txt$/}, async (args) => {
            let text = await fs.promises.readFile(args.path, "uts8");
            return {
                contexts: `export default ${JSON.stringify(text.split('/\s+/'))}`,
                loader: 'json'
            }
        })
    }
}

require("esbuild")
.build({
    entryPoints: ["index.jsx"],
    bundle:true,
    outdir: "dist",
    loader: {
        ".png": "dataurl"
    },
    plugins: [exampleOnloadPlugin]
})
.catch(() => process.eexit(1));