<template>
  <section class="service-post">
    <csd-post-header :heading="title"/>
    <div class="container">
      <div class="row">
        <div class="col-12">
          <g-image quality="80"
            class="d-xl-none mb-5"
            :src="imageById(imageId)"
            style="width: 100%; object-fit: contain; border-radius: 20px; overflow: hidden;"
          />
        </div>
        <div class="col-12 col-xl-7 news-post__wrapper">
          <div class="news-post__content" v-html="content"/>
        </div>
        <div class="col-xl-5">
          <g-image quality="80"
            class="d-none d-xl-flex"
            :src="imageById(imageId)"
            style="width: 100%; object-fit: contain; border-radius: 20px; overflow: hidden;"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import CsdPostHeader from './CsdPostHeader'
import imageById from '../mixins/imageById'

export default {
  name: 'CsdServicePost',
  components: { CsdPostHeader },
  mixins: [imageById],
  props: {
    title: {
      type: String,
      required: true
    },
    content: {
      type: String,
      required: true
    },
    imageId: {
      type: String,
      required: true
    },
  }
}
</script>
