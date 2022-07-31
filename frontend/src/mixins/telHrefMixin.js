export default {
  methods: {
    getTelHref(tel) {
      const _tel = tel
        .replaceAll('-', '')
        .replaceAll('(', '')
        .replaceAll(')', '')
        .replaceAll(' ', '')
      return `tel:${_tel}`
    }
  }
}
