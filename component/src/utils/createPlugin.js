// 1. 创建传入的组件实例
// 2.挂载它从而生成dom结构
// 3。生成dom结构，追加到body
// 4. t淘汰机制 ： 不需要时候组件实例应当被销毁
import Vue from 'vue'

export default function create(Component, props) {
    const Ctor = Vue.extend(Component)
    const comp = new Ctor({propsData: props})
    comp.$mount();
    document.body.appendChild(comp.$el)
    comp.remove = () => { // 移除dom document.body.removeChild(comp.$el) // 销毁组件
       comp.$destroy();
    }
    return comp
}