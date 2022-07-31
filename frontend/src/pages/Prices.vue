<template>
  <Layout>
    <csd-post-header
      heading="Цены"
      subheading="(Стоимость зависит от объёма запущенных работ)"
    />
    <div class="container mb-5">
      <div class="row">
        <div class="col-12 col-xl-8 price-list-table-wrapper">
          <csd-price-list/>
        </div>
        <div class="col-12 col-xl-3 offset-xl-1">
          <div class="price-calc-wrapper mt-5 mt-xl-0 mx-auto ml-xl-auto">
            <csd-price-calc-form class="ml-auto"/>
            <span class="price-calc-wrapper__phone-title">Либо уточните по номеру телефона:</span>
            <a href="tel:88006001744" class="price-calc-wrapper__phone">8 (800) 600-17-44</a>
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
import CsdBackwardButton from '../components/CsdBackwardButton'
import CsdPostHeader from '../components/CsdPostHeader'
import CsdPriceList from '../components/CsdPriceList'
import CsdPriceCalcForm from '../components/CsdPriceCalcForm'

export default {
  name: 'Prices',
  components: { CsdPriceCalcForm, CsdPriceList, CsdPostHeader, CsdBackwardButton }
}
</script>
