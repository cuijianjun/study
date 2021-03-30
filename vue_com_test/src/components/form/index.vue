<template>
  <div>
    <!-- KFrom: 指定管理数据和校验规则 -->
    <!-- KFromItem: 数据校验和错误展示 -->
    <KForm :model="model" :rules="rules" ref="loginForm">
      <KFormItem label="用户名" prop="username">
        <KInput v-model="model.username" placeholder="请输入账户"></KInput>
      </KFormItem>
      <KFormItem label="密码" prop="password">
        <KInput v-model="model.password" placeholder="请输入密码" type="password"></KInput>
      </KFormItem>
      <KFormItem><button @click="login">登录</button></KFormItem>
    </KForm>
  </div>
</template>

<script>
  import KInput from '@/components/form/KInput'
  import KFormItem from '@/components/form/KFormItem'
  import KForm from '@/components/form/KForm'

  import Notice from "@/components/Notice.vue"
  import create from "@/utils/create"

  export default {
    name: 'HelloWorld',
    components: {
      KInput,
      KFormItem,
      KForm
    },
    props: {
      msg: String
    },
    data() {
      return {
        model: {
          username: 'tom',
          password: ''
        },
        rules: {
          username: [{
            required: true,
            message: '必须输入用户名'
          }],
          password: [{
            required: true,
            message: '必须输入密码'
          }]
        }
      }
    },
    methods: {
      login() {
        this.$refs.loginForm.validate(isVaild => {
          // if (isVaild) {
          //   console.log("提交登录");
          // } else {
          //   console.log("登录失败");
          // }
          create(Notice, {
            title: '军哥6',
            message: isVaild? '请求登录': '校验失败'
          }).show()
        })
      }
    },
  }
</script>

<style>

</style>