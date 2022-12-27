export default (enforce?: 'pre' | 'post') => {
  return {
    name: 'test',
    config(userConfig) {
      return {
        resolve: {
          alias: {
            '@aaa': '/src/styles',
          },
        },
      }
    },
    configResolved(config) {
      console.log(config.resolve)
    },
    configureServer(server){
        server.middlewares.use((req, res, next) => {
            if (req.url === '/test') {
                res.end('hello vite')
            } else {
                next();
            }
        })
    },
    transformIndexHtml(html) {
        console.log(html);
    },
    handleHotUpdata(ctx) {
        console.log(ctx);
        ctx.server.ws.send({
            type: "custom",
            event: 'test'
        })
    }
  }
}
 