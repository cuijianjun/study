import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

import testPlugin from "./plugins/test-plugin"
import viteMdx from './plugins/vite-mdx'
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    viteMdx(),
    vueJsx(
      {
        include: /\.(jsx|tsx|mdx)/
      }),],
  resolve: {
    alias: {
      "@styles": "/src/styles",
    }
  }
})
