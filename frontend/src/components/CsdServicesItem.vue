<template>
  <article class="service">
    <div class="service__icon">
      <g-image quality="80" :src="icon" alt=""/>
    </div>
    <div class="service__image-wrapper">
      <g-image quality="80" :src="image.toString()"/>
    </div>
    <div class="service__name-wrapper">
      <span :title="name" class="service__name">{{ name }}</span>
    </div>
    <div class="service__link-wrapper">
      <g-link class="service__link" :to="to">Подробнее</g-link>
    </div>
  </article>
</template>

<script lang="ts">
export default {
  name: 'CsdServicesItem',
  props: {
    to: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    image: {
      type: String,
      required: true
    }
  }
}
</script>
