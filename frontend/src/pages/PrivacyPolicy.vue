<template>
  <Layout>
    <csd-empty-page
      :title="privacy.title"
      :content="privacy.content"
    />
  </Layout>
</template>

<script>
import privacy from './privacy.json'
import CsdEmptyPage from '../components/CsdEmptyPage'

export default {
  name: 'PrivacyPolicy',
  components: { CsdEmptyPage },
  data() {
    return {
      privacy
    }
  }
}
</script>
