<template>
  <section class="our-clients" id="clients">
    <div class="container">
      <div class="circle"/>
      <div class="row">
        <div :class="[{'col-10': windowSize.width>breakpoint, 'col-12': windowSize.width<=breakpoint}]">
          <h2 class="our-clients__heading">Наши клиенты</h2>
        </div>
        <div
          class="col-2"
          v-if="windowSize.width > breakpoint">
          <csd-slider-arrows
            @prev="handleSlidePrev"
            @next="handleSlideNext"
          />
        </div>
      </div>
      <div class="row mt-5">
        <div class="col-12">
          <div class="swiper swiper-clients">
            <div class="swiper-wrapper">
              <template v-for="{node} in $static.allClients.edges">
                <div class="swiper-slide d-flex align-self-stretch">
                  <div class="client align-self-stretch">
                    <div class="client__logo">
                      <div class="client__image">
                        <g-image quality="80"
                          :alt="node.title"
                          :src="imageById(node.image_id)"
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-4" v-if="windowSize.width <= breakpoint">
        <div class="col-12">
          <csd-slider-arrows
            class="mx-auto"
            @prev="handleSlidePrev"
            @next="handleSlideNext"
          />
        </div>
      </div>
    </div>
  </section>
</template>
<static-query>
query {
  allClients {
    edges {
      node {
        id
        title
        image_id
      }
    }
  }
}
</static-query>
<script>
import 'swiper/swiper.scss'
import Swiper from 'swiper'
import IconChevronLeft from './icons/IconChevronLeft.vue'
import IconChevronRight from './icons/IconChevronRight.vue'
import CsdSliderArrows from './CsdSliderArrows'
import windowSizeMixin from '../mixins/windowSizeMixin'
import imageById from '../mixins/imageById'

export default {
  name: 'CsdSectionOurClients',
  mixins: [windowSizeMixin, imageById],
  components: { CsdSliderArrows, IconChevronRight, IconChevronLeft },
  data() {
    return {
      swiper: null,
      breakpoint: 768
    }
  },
  methods: {
    handleSlidePrev() {
      this.swiper.slidePrev()
    },
    handleSlideNext() {
      this.swiper.slideNext()
    }
  },
  mounted() {
    this.swiper = new Swiper('.swiper-clients', {
      loop: true,
      speed: 400,
      spaceBetween: 8,
      slidesPerView: 2,
      breakpoints: {
        445: {
          slidesPerView: 3,
          spaceBetween: 20
        },
        889: {
          slidesPerView: 4,
          spaceBetween: 20
        },
        1400: {
          slidesPerView: 5,
          spaceBetween: 20
        },
        1600: {
          slidesPerView: 6,
          spaceBetween: 20
        }
      }
    })
  }
}
</script>
