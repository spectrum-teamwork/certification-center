<template>
  <Layout>
    <template v-if="$page.services">
      <csd-service-post
        :price="$page.services.price"
        :heading="$page.services.title"
        :content="$page.services.description"
        :cert-image="imageById($page.services.image_document_id)"
        :requirements="$page.services.requirements"
        :requirements-heading="requirementsHeadings[$page.services.service_type]"
      />
    </template>
  </Layout>
</template>
<page-query>
query ($serviceId: ID) {
  services (id: $serviceId) {
    id
    price
    title
    description
    service_type
    requirements
    image_document_id
  }
}
</page-query>
<script>
import CsdPageFooter from '~/components/CsdPageFooter'
import CsdHeader from '~/components/CsdHeader'
import CsdBackwardButton from '~/components/CsdBackwardButton'
import CsdServicePost from '../../components/CsdServicePost'
import imageById from '../../mixins/imageById'

export default {
  name: 'Service',
  mixins: [imageById],
  data() {
    return {
      requirementsHeadings: {
        testing: 'Для регистрации декларации и получения протокола испытаний, требуется',
        certification: 'Для регистрации декларации и получения протокола испытаний, требуется',
      }
    }
  },
  components: { CsdServicePost, CsdBackwardButton, CsdHeader, CsdPageFooter }
}
</script>

<style lang="scss">

</style>