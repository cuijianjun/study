<template>
  <div>
    <FormExample></FormExample>
  </div>
</template>

<script>
import FormExample from '@/components/form'
export default {
  name: 'HelloWorld',
  components: {
    FormExample
  },
  props: {
    msg: String
  },
  data () {
    return {
      model: {
        usename: 'tom',
        password: ''
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
