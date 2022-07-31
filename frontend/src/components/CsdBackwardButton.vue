<template>
  <a href="#" @click.prevent="$router.back()">
    <g-image quality="80" src="/assets/img/backward.svg" alt="Указатель на предыдущуюю страницу"/>
  </a>
</template>

<script>
export default {
  name: 'CsdBackwardButton'
}
</script>
