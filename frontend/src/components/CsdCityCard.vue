<template>
  <div class="csd-city-card">
    <p class="csd-city-card__contact-heading" v-text="`г. ${city}`"/>
    <div class="csd-city-card__contact-row">
      <icon-phone class="csd-city-card__contact-icon"/>
      <a class="csd-city-card__contact-data" :href="`tel:${formattedPhone}`" v-text="phone"/>
    </div>
    <div class="csd-city-card__contact-row">
      <icon-location class="csd-city-card__contact-icon"/>
      <span class="csd-city-card__contact-data" v-text="address"/>
    </div>
    <div class="csd-city-card__contact-row">
      <icon-envelope class="csd-city-card__contact-icon"/>
      <a class="csd-city-card__contact-data" :href="`mailto:${email}`" v-text="email"/>
    </div>
    <iframe
      :src="map" frameborder="0"
      width="100%"
      height="285"
    />
  </div>
</template>

<script>
import IconPhone from './icons/IconPhone'
import IconLocation from './icons/IconLocation'
import IconEnvelope from './icons/IconEnvelope'
import telHrefMixin from '../mixins/telHrefMixin'

export default {
  name: 'CsdCityCard',
  mixins: [telHrefMixin],
  components: { IconEnvelope, IconLocation, IconPhone },

  props: {
    city: {
      type: String,
      default: null
    },
    phone: {
      type: String,
      default: null
    },
    email: {
      type: String,
      default: null
    },
    address: {
      type: String,
      default: null
    },
    map: {
      type: String,
      default: null
    }
  },
  computed: {
    formattedPhone() {
      return this.getTelHref(this.phone)
    }
  }
}
</script>

<style lang="scss">

</style>