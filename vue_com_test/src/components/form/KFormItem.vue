<template>
  <div>
    <!-- label -->
    <label v-if="label">{{label}}</label>
    <slot></slot>
    <!-- 错误信息 -->
    <p class="error" v-if="error">{{error}}</p>
  </div>
</template>

<script>
import Validator from "async-validator";
import emitter from '@/mixins/emitter';

export default {
  name: 'KFormItem',
  componentName: 'KFormItem',
  mixins: [emitter],
  inject: ["form"],
  data() {
    return {
      error: ""
    };
  },
  props: {
    label: {
      type: String,
      default: ""
    },
    prop: String
  },
  mounted() {
    // 派发事件通知KForm， 新增一个KFormItem的实例
    this.dispatch('KForm', 'kkb.form.addField', [this])
    this.$on("validate", () => {
      this.validate();
    });
  },
  methods: {
    validate() {
      // 校验规则
      const rules = this.form.rules[this.prop];
      // 当前值
      const value = this.form.model[this.prop];

      // 创建一个校验器实例
      const validator = new Validator({ [this.prop]: rules });
      // 校验, 返回Promise
      return validator.validate({ [this.prop]: value}, errors => {
        if (errors) {
          this.error = errors[0].message
        } else {
          this.error = ''
        }
      })
    }
  }
};
</script>

<style scoped>
.error {
  color: red;
}
</style>