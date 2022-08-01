<template>
  <Layout>
    <csd-empty-page
      :title="user.title"
      :content="user.content"
    />
  </Layout>
</template>

<script>
import user from './user.json'
import CsdEmptyPage from '../components/CsdEmptyPage'

export default {
  name: 'UserAgreement',
  components: { CsdEmptyPage },
  data() {
    return {
      user
    }
  }
}
</script>
