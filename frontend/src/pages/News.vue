<template>
  <Layout>
    <csd-news-post/>
  </Layout>
</template>
<script>
import CsdPageFooter from '~/components/CsdPageFooter'
import CsdHeader from '~/components/CsdHeader'
import CsdBackwardButton from '~/components/CsdBackwardButton'
import CsdNewsPost from '../components/CsdNewsPost'

export default {
  name: 'NewsPost',
  components: { CsdNewsPost, CsdBackwardButton, CsdHeader, CsdPageFooter }
}
</script>
