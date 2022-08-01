<template>
  <div class="container">
    <div class="row">
      <div class="col-12 col-lg-8 col-xxl-6">
        <div class="hero">
          <h1 class="hero__title" v-html="$static.hero.title"/>
          <p class="hero__description" v-html="$static.hero.text"/>
          <div class="hero__actions">
            <div @click="handleModalLeaveOrderOpen" class="button button__order">Заказать</div>
            <span @click="handleModalConsultationOpen" class="hero__link">Проконсультироваться</span>
          </div>
        </div>
      </div>
    </div>
    <csd-modal v-model="leaveOrderModalVisible">
      <div class="col-12 col-md-10 col-lg-10 col-xl-9 col-xxl-8 col-xxxl-7 mx-auto">
        <csd-leave-order-form @close="handleModalLeaveOrderClose" closeable class="mx-auto"/>
      </div>
    </csd-modal>
    <csd-modal v-model="consultationModalVisible">
      <div class="col-12 col-md-10 col-lg-10 col-xl-9 col-xxl-8 col-xxxl-7 mx-auto">
        <csd-consultation-form @close="handleModalConsultationClose" closeable class="mx-auto"/>
      </div>
    </csd-modal>
  </div>
</template>
<static-query>
query {
  hero(id: "1") {
    title
    text
  }
}
</static-query>
<script>
import CsdModal from './CsdModal'
import CsdLeaveOrderForm from './CsdLeaveOrderForm'
import CsdConsultationForm from './CsdConsultationForm'

export default {
  name: 'CsdHero',
  components: { CsdConsultationForm, CsdLeaveOrderForm, CsdModal },
  data() {
    return {
      leaveOrderModalVisible: false,
      consultationModalVisible: false
    }
  },
  methods: {
    handleModalLeaveOrderOpen() {
      this.leaveOrderModalVisible = true
    },
    handleModalConsultationOpen() {
      this.consultationModalVisible = true
    },
    handleModalLeaveOrderClose() {
      this.leaveOrderModalVisible = false
    },
    handleModalConsultationClose() {
      this.consultationModalVisible = false
    }
  }
}
</script>
