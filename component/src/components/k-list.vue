<template>
  <div class="list-view" @scroll="handleScroll">
    <div class="list-view-phantom" :style="{height: contentHeight}">
      <div ref="content" class="list-view-content">
        <div
          class="list-view-item"
          :style="{height: itemHeight + 'px'}"
          v-for="item in visbleData"
          :key="item.value"
        >{{item.value}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'k-list',
  data: () => (
    {
      visbleData: []
    }
  ),
  props: {
    data: {
      type: Array,
      required: true
    },
    itemHeight: {
      type: Number,
      default: 30

    }
  },
  methods: {
    handleScroll () {
      const scrollTop = this.$el.scrollTop
      this.calculateVisibleData(scrollTop)
    },
    calculateVisibleData (scrollTop = 0) {
      // 根据偏移量，计算可见数据
      console.log('666666')
      const visbleCount = Math.ceil(this.$el.clientHeight / this.itemHeight)
      // 开始的索引
      const start = Math.floor(scrollTop / this.itemHeight)
      const end = start + visbleCount
      this.visbleData = this.data.slice(start, end)
      this.$refs.content.style.webkitTransform = `translate3d(0, ${start * this.itemHeight}px, 0)`
    }
  },
  mounted () {
    // 计算可是区域
    this.calculateVisibleData()
  },
  computed: {
    contentHeight () {
      // 内容的高度
      return (this.data.length * this.itemHeight) + 'px'
    }
  }
}
</script>

<style scoped>
  .list-view {
    height: 400px;
    overflow: auto;
    position: relative;
    border: 1px solid #aaa;
  }

  .list-view-phantom {
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    z-index: -1;
  }

  .list-view-content {
    left: 0;
    right: 0;
    top: 0;
    position: absolute;
  }

  .list-view-item {
    padding: 5px;
    color: #666;
    line-height: 30px;
    box-sizing: border-box;
  }
</style>
