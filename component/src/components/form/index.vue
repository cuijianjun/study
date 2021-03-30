<template>
    <div>
        <k-form :model="model" :rules="rules" ref="loginForm">
            <k-form-item label="用户名" prop="username">
                <k-input v-model="model.username" placeholder="请输入用户名" @change="handleClick(model.username)"></k-input>
            </k-form-item>
            <k-form-item label="密码" prop="password">
                <k-input v-model="model.password" type="password"></k-input>
            </k-form-item>
            <k-form-item>
                <button @click="onLogin">提交</button>
            </k-form-item>
        </k-form>
    </div>
</template>

<script>
    import KInput from '@/components/form/Kinput.vue'
    import KFormItem from '@/components/form/KFormItem.vue'
    import KForm from '@/components/form/KForm.vue'
    import Notice from "@/components/notice/Notice";
    export default {
        name: 'index',
        data() {
            return {
                model: {
                    username: '',
                    password: ''
                },
                rules: {
                    username: [
                        {
                            required: true,
                            message: '必填项'
                        },
                    ],
                    password: [
                        {
                            required: true,
                            message: '必填项222'
                        }
                    ]

                }
            }
        },
        methods: {
            onLogin() {
                this.$refs.loginForm.validate( isValid => {
                    this.$create(Notice, {
                        title: "社会你杨哥喊你来搬砖",
                        message: isValid?"提请求登录！":"校验失败！",
                        duration: 2000
                    }).show();
                })
            },
            handleClick(val) {
                console.log(val)
            }
        },
        components: {
            KInput, KFormItem, KForm
        }
    }
</script>

<style scoped>

</style>
