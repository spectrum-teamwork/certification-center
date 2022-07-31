<template>
  <header
    :class="['header', {'header_hero': isHero}]">
    <div class="container">
      <div class="row">
        <div class="col-8 col-sm-4 col-md-4 col-lg-3 col-xxl-2 my-auto">
          <div class="logo">
            <g-link to="/">
              <g-image quality="80" src="/assets/img/logo.svg" alt="Логотип Центра сертификации и декларирования"/>
            </g-link>
          </div>
        </div>
        <div class="col-4 col-sm-8 col-md-8 col-xxl-10 align-items-center justify-content-between">
          <csd-region-select class="d-none d-sm-flex mx-auto mt-4 mx-sm-0 mt-sm-0 d-xxl-none"/>
          <csd-navigation class="d-none ml-auto d-xxl-flex"/>
          <div class="ml-auto d-xxl-none">
            <client-only>
              <csd-side-menu width="100%">
                <csd-navigation/>
              </csd-side-menu>
            </client-only>
          </div>
        </div>
      </div>
      <div class="row d-sm-none">
        <div class="col-12">
          <csd-region-select class="mt-4"/>
        </div>
      </div>
      <div class="row d-none d-xxl-flex">
        <div class="col-12 mt-4">
          <csd-region-select/>
        </div>
      </div>
      <template v-if="$route.path !== '/'">
        <div class="row">
          <div class="col-1 pt-5 pb-5">
            <csd-backward-button/>
          </div>
        </div>
      </template>
    </div>
    <slot name="hero"/>
  </header>
</template>
<script>
import CsdRegionSelect from './CsdRegionSelect'
import CsdNavigation from './CsdNavigation'
import CsdBackwardButton from './CsdBackwardButton'
import CsdSideMenu from './CsdSideMenu'

export default {
  name: 'CsdHeader',
  components: { CsdSideMenu, CsdBackwardButton, CsdRegionSelect, CsdNavigation },
  data() {
    return {
      regionId: '0',
      regions: [],
      cookies: null
    }
  },
  computed: {
    isHero() {
      return !!this.$slots['hero']
    }
  }
}
</script>
