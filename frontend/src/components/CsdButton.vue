<template>
  <component :disabled="loading" @click="$emit('click')" :is="tag" :class="classes">
    <slot v-if="!loading">
      {{ label }}
    </slot>
    <template v-else>
      <span class="op-0">spinner</span>
      <svg class="spinner" viewBox="0 0 50 50">
        <circle class="path" cx="25" cy="25" r="20" fill="none" stroke-width="5"></circle>
      </svg>
    </template>
  </component>
</template>

<script>
export default {
  name: 'CsdButton',
  props: {
    tag: {
      type: String,
      default: 'button'
    },
    loading: {
      type: Boolean,
      default: false
    },
    label: {
      type: String,
      default: 'Submit'
    }
  },
  computed: {
    classes() {
      return {
        'button': true,
        'button_loading': this.loading
      }
    }
  }
}
</script>
