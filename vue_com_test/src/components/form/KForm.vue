<template>
  <div>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'KForm',
  componentName: 'KForm',
  provide() {
    return {
      form: this
    };
  },
  created() {
    this.fields = [];
    this.$on('kkb.form.addField', item => {
      if (item.prop) {
        this.fields.push(item)
      }
    })
  },
  props: {
    model: {
      type: Object,
      required: true
    },
    rules: Object
  },
  methods: {
    validate(cb) {
      // 检查所有表单项目
      // 他们都要校验通过
      // 获得一个Promise数组
      // const tasks = this.$children
      //   .filter(item => item.prop) // 必须拥有prop属性的FormItem留下
      //   .map(item => item.validate());
      const tasks = this.fields.map(item => item.validate());
      Promise.all(tasks)
        .then(() => cb(true))
        .catch(() => cb(false));
    }
  }
};
</script>

<style lang="scss" scoped>
</style>