<template>
  <Layout>
    <csd-post-header heading="Контакты"/>
    <div class="container container_contacts-page">
      <div class="row">
        <div
          v-for="{node} in $static.allAddresses.edges"
          class="col-12 col-lg-6">
          <csd-city-card
            :city="node.city"
            :phone="node.phone"
            :address="node.address"
            :email="node.email"
            :map="node.place_src"
          />
        </div>
      </div>
    </div>
    <csd-leave-order-section/>
  </Layout>
</template>
<static-query>
query addresses {
  allAddresses {
    edges {
      node {
        id
        region
        city
        address
        phone
        email
        place_src
      }
    }
  }
}
</static-query>
<script>
import CsdPostHeader from '../components/CsdPostHeader'
import CsdLeaveOrderSection from '../components/CsdLeaveOrderSection'
import CsdCityCard from '../components/CsdCityCard'

export default {
  name: 'Contacts',
  components: { CsdCityCard, CsdPostHeader, CsdLeaveOrderSection }
}
</script>

<style lang="scss">

</style>