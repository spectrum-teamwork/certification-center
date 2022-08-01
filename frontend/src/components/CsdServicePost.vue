<template>
  <section class="service-post">
    <csd-post-header :heading="heading"/>
    <div class="container">
      <div class="row d-lg-none">
        <div class="col-12">
          <div class="price-calc-wrapper">
            <span class="price-calc-wrapper__price">от {{ price }} ₽</span>
            <span class="price-calc-wrapper__description">Стоимость зависит от объёма запущенных работ</span>
          </div>
        </div>
      </div>
      <div class="row mb-4 d-lg-none">
        <div class="col-12">
          <div class="requirements">
            <div class="ml-0 requirements__content">
              <h3
                class="requirements__heading"
                v-html="requirementsHeading"
              />
              <p class="requirements__text" v-html="requirements"/>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="d-none d-lg-flex col-lg-7 service-post__wrapper">
          <div class="service-post__content" v-html="content"/>
          <div class="requirements d-none d-lg-flex">
            <div class="requirements__cert">
              <g-image quality="80" id="image" :src="certImage" alt="Пример сертификата/протокола испытаний"/>
            </div>
            <div class="requirements__content">
              <h3
                class="requirements__heading"
                v-html="requirementsHeading"
              />
              <p class="requirements__text" v-html="requirements"/>
            </div>
          </div>
        </div>
        <div class="col-12 col-lg-4 offset-lg-1">
          <div class="price-calc-wrapper mx-auto mr-lg-0 ml-lg-auto">
            <span class="d-none d-lg-block price-calc-wrapper__price">от {{ price }} ₽</span>
            <span
              class="d-none d-lg-block price-calc-wrapper__description">Стоимость зависит от объёма запущенных работ</span>
            <csd-price-calc-form/>
            <span class="price-calc-wrapper__phone-title">Либо уточните по номеру телефона:</span>
            <a href="tel:88006001744" class="price-calc-wrapper__phone">8 (800) 600-17-44</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import 'viewerjs/dist/viewer.css'
import CsdPostHeader from './CsdPostHeader'
import CsdPriceCalcForm from './CsdPriceCalcForm'
import Viewer from 'viewerjs'

export default {
  name: 'CsdServicePost',
  components: { CsdPriceCalcForm, CsdPostHeader },
  props: {
    price: {
      type: Number,
      required: true
    },
    heading: {
      type: String,
      required: true
    },
    content: {
      type: String,
      required: true
    },
    certImage: {
      type: String,
      required: true
    },
    requirements: {
      type: String,
      required: true
    },
    requirementsHeading: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      viewer: undefined
    }
  },
  mounted() {
    this.viewer = new Viewer(document.getElementById('image'), {
      viewed() {
        this.viewer.zoomTo(1)
      }
    })
  }
}
</script>
<style lang="scss">
.viewer-toolbar {
  ul {
    li {
      display: flex;
    }
  }
}
</style>