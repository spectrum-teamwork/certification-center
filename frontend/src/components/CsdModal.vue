<template>
  <transition name="fade" v-if="value">
    <div class="modal">
      <div class="container">
        <div class="row">
          <slot/>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'CsdModal',
  props: {
    value: {
      type: Boolean,
      default: false
    }
  }
}
</script>

