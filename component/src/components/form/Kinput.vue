<template>
    <div>
        <input :type="type" @input="onInput" :value="value" v-bind="$attrs">
    </div>
</template>

<script>
    export default {
        name: 'Kinput',
        inheritAttrs: false,
        props: {
            value: {
                type: String,
                default: ''

            },
            type: {
                type: String,
                default: ''

            }
        },
        methods: {
            onInput(e) {
                this.$emit('input', e.target.value)
                this.$parent.$emit('validate')
            }
        }
    }
</script>

<style scoped>

</style>
