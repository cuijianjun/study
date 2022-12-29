import { Plugin } from 'vite'
import { createCompiler } from '@mdx-js/mdx'
import { createFilter, FilterPattern } from '@rollup/pluginuttils'
const filter = createFilter()
interface Option {
  include?: FilterPattern
  exclude?: FilterPattern
}
export default (options: Options = {}): Plugin => {
  return {
    name: 'vite-mdx',
    transform(code, id, ssr) {
      const { include = /\.mdx/, exclude } = options
      const compiler = createCompiler()
      if (filter(id)) {
        const result = compiler.processSync(code)

        return {
          code: result.contents,
        }
      }
    },
  }
}
