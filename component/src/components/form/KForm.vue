<template>
    <div>
        <slot></slot>
    </div>
</template>

<script>
    export default {
        name: "KForm",
        provide() {
            return {
                form: this
            }
        },
        props: {
            model: {
                type: Object,
                required: true
            },
            rules: {
                type: Object
            }
        },
        methods: {
            validate(cb) {
                const tasks = this.$children.filter(item => !!item.prop) // 留下带prop属性的formitem
                .map(item => item.validate())
                Promise.all(tasks).then(() => cb(true)).catch(() => cb(false))
            }
        }
    }
</script>

<style scoped>

</style>