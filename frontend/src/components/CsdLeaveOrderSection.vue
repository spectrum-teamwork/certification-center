<template>
  <section class="leave-order">
    <div class="container">
      <div class="row">
        <div class="leave-order__network">
          <g-image quality="80" src="/assets/img/network.svg"/>
        </div>
        <div class="col-12 col-lg-10 col-xl-9 col-xxl-8 col-xxxl-7">
          <csd-leave-order-form/>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import CsdLeaveOrderForm from './CsdLeaveOrderForm'

export default {
  name: 'CsdLeaveOrderSection',
  components: { CsdLeaveOrderForm }
}
</script>
