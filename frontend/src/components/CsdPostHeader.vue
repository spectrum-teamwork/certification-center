<template>
  <div class="container">
    <div class="row">
      <div class="col-12 post-header pb-5">
        <h1
          class="post-header__heading">
          {{ heading }}
        </h1>
        <span
          v-if="subheading"
          class="post-header__subheading">
          {{ subheading }}
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CsdPostHeader',
  props: {
    heading: {
      type: String,
      required: true
    },
    subheading: {
      type: String,
      default: null
    }
  }
}
</script>
