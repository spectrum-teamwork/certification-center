<template>
  <div class="slider-arrows">
    <button
      @click="$emit('prev')"
      class="slider-arrows__prev"
    >
      <icon-chevron-left/>
    </button>
    <button
      @click="$emit('next')"
      class="slider-arrows__next"
    >
      <icon-chevron-right/>
    </button>
  </div>
</template>

<script>
import IconChevronLeft from './icons/IconChevronLeft'
import IconChevronRight from './icons/IconChevronRight'

export default {
  name: 'CsdSliderArrows',
  components: { IconChevronRight, IconChevronLeft }
}
</script>
