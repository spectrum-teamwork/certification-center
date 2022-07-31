<template>
  <section class="news">
    <div class="container">
      <div class="row">
        <div :class="[{'col-10': windowSize.width >= breakpoint, 'col-12': windowSize.width < breakpoint}]">
          <h2>Новости</h2>
        </div>
        <div class="col-2" v-if="windowSize.width >= breakpoint">
          <csd-slider-arrows
            @prev="handleSlidePrev"
            @next="handleSlideNext"
          />
        </div>
      </div>
      <div class="row mt-5">
        <div class="col-12">
          <div class="swiper swiper-news">
            <div class="swiper-wrapper">
              <template v-for="{node} in $static.allNews.edges">
                <div class="swiper-slide d-flex align-items-stretch">
                  <div class="post">
                    <div
                      class="post__image"
                      :style="{backgroundImage: `url('${node.image}')`}"
                    />
                    <div class="post__text-wrapper">
                      <div class="post__heading">
                        {{ node.heading }}
                      </div>
                      <p class="post__highlight">
                        {{ node.highlight }}
                      </p>
                      <g-link to="/news" class="post__link">Подробнее</g-link>
                    </div>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
      <div class="row" v-if="windowSize.width < breakpoint">
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
  allNews {
    edges {
      node {
        id
        image
        heading
        highlight
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

export default {
  name: 'CsdSectionNews',
  mixins: [windowSizeMixin],
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
    this.swiper = new Swiper('.swiper-news', {
      speed: 400,
      loop: true,
      slidesPerView: 2,
      spaceBetween: 10,
      breakpoints: {
        992: {
          slidesPerView: 3,
          spaceBetween: 20
        },
        1400: {
          slidesPerView: 4,
          spaceBetween: 20
        }
      }
    })
  }
}
</script>
