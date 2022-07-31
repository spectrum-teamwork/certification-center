<template>
  <Layout>
    <csd-section-about/>
    <csd-section-services/>
    <csd-section-our-clients/>
    <csd-accreditation-section/>
    <csd-section-news/>
    <csd-leave-order-section/>
  </Layout>
</template>

<script>
import CsdSectionAbout from '../components/CsdSectionAbout'
import CsdSectionServices from '../components/CsdSectionServices'
import CsdSectionOurClients from '../components/CsdSectionOurClients'
import CsdAccreditationSection from '../components/CsdAccreditationSection'
import CsdSectionNews from '../components/CsdSectionNews'
import CsdLeaveOrderSection from '../components/CsdLeaveOrderSection'

export default {
  components: {
    CsdLeaveOrderSection,
    CsdSectionNews,
    CsdAccreditationSection,
    CsdSectionOurClients,
    CsdSectionServices,
    CsdSectionAbout
  },

  metaInfo: {
    title: 'Главная'
  }
}
</script>
