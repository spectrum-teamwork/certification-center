<template>
  <div class="container">
    <div class="row">
      <div class="col-12 col-lg-8 col-xxl-6">
        <div class="hero">
          <h1 class="hero__title">
            Испытания<br/>и сертификация<br/>продукции
          </h1>
          <p class="hero__description">
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
            industry's
            standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to
            make a type specimen book.
          </p>
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
      consultationModalVisible: false,
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
