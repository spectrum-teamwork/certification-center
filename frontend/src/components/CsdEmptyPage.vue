<template>
  <section class="service-post">
    <csd-post-header :heading="title"/>
    <div class="container">
      <div class="row">
        <div class="col-12 news-post__wrapper">
          <div class="news-post__content" v-html="content"/>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import CsdPostHeader from './CsdPostHeader'

export default {
  name: 'CsdEmptyPage',
  components: { CsdPostHeader },
  props: {
    title: {
      type: String,
      required: true
    },
    content: {
      type: String,
      required: true
    }
  }
}
</script>
