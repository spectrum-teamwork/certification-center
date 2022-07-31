export default {
  methods: {
    onRegionUpdate(fn) {
      addEventListener('onregionupdate', fn)
    }
  }
}