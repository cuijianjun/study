<template>
<!--  <KList :data="data"></KList>-->
<kform ></kform>
</template>

<script>
// @ is an alias to /src
// import KList from '@/components/k-list'
import Kform from '@/components/form'

export default {
  name: 'Home',
  props: {
   name: {
     type: String,
     default: 'aaaa'
   }
  },

  components: {
    Kform
  },
  data () {
    return {
      a: this.name
    }
  },
  mounted() {
    console.log(this.a)
  }
}
</script>
