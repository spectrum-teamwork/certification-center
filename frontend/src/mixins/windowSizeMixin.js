export default {
  data() {
    return {
      windowSize: {
        width: 0,
        height: 0
      }
    }
  },
  methods: {
    onWindowResize() {
      this.windowSize.width = window.innerWidth
      this.windowSize.height = window.innerHeight
    }
  },
  beforeDestroy() {
    removeEventListener('resize', this.onWindowResize)
  },
  mounted() {
    this.onWindowResize()
    window.addEventListener('resize', this.onWindowResize)
  }
}