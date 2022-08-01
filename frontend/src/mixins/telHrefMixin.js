export default {
  methods: {
    getTelHref(tel) {
      console.log(tel)
      const _tel = tel
        .replaceAll('-', '')
        .replaceAll('(', '')
        .replaceAll(')', '')
        .replaceAll(' ', '')
      return `tel:${_tel}`
    }
  }
}
