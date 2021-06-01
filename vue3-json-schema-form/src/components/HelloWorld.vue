<template>
  <div class="hello">
    {{age}}
  </div>
</template>

<script lang="ts">
  import { defineComponent } from "vue";
  const PropsType = {
    msg: String,
    age: {
      type: Number,
      require: true
    }
  } // 只读属性的更改方法  as const

  export default defineComponent({
    name: "HelloWorld",
    props: PropsType,
    mounted() {
      this.age
    },
  });
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