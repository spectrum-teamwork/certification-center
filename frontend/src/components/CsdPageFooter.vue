<template>
  <footer class="footer">
    <div class="container">
      <div class="row">
        <div class="col-12 col-lg-2">
          <div class="logo">
            <g-image quality="80" src="/assets/img/logo-white.svg" alt="Логотип Центра сертификации и декларирования"/>
          </div>
        </div>
        <div class="col-12 col-lg-8 offset-lg-2">
          <div class="footer__requisites">
            <span v-text="$static.requisites.name"></span>
            <span class="ml-5" v-text="`ИНН: ${$static.requisites.inn}`"></span>
            <span class="ml-5" v-text="`ОГРН: ${$static.requisites.ogrn}`"></span>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12 col-lg-3 mt-4 mt-lg-0 footer__policies">
          <g-link to="/privacy-policy">Политика конфиденциальности</g-link>
          <g-link to="/user-agreement">Пользовательское соглашение</g-link>
        </div>
        <template v-if="$static.allAddresses.edges.length >= 1">
          <div class="col-12 mt-4 mt-lg-0 col-lg-5 offset-lg-1 d-flex flex-column">
            {{ $static.allAddresses.edges[0].node.city }}:
            <a
              :href="getTelHref($static.allAddresses.edges[0].node.phone)">{{
                $static.allAddresses.edges[0].node.phone
              }}</a>
            {{ $static.allAddresses.edges[0].node.address }}
            <a href="mailto:krd@csd.expert">{{ $static.allAddresses.edges[0].node.email }}</a>
          </div>
        </template>
        <template v-if="$static.allAddresses.edges.length >= 2">
          <div class="col-12 mt-4 mt-lg-0 col-lg-3 d-flex flex-column">
            {{ $static.allAddresses.edges[1].node.city }}:
            <a :href="getTelHref($static.allAddresses.edges[1].node.phone)"
               class="text-white">{{ $static.allAddresses.edges[1].node.phone }}</a>
            {{ $static.allAddresses.edges[1].node.address }}
            <a href="mailto:krd@csd.expert" class="text-white">{{ $static.allAddresses.edges[1].node.email }}</a>
          </div>
        </template>
      </div>
    </div>
  </footer>
</template>
<static-query>
query {
  requisites(id: "1") {
    name
    inn
    ogrn
  }
  allAddresses {
    edges {
      node {
        id
        city
        address
        phone
        email
      }
    }
  }
}
</static-query>
<script>
import telHrefMixin from '../mixins/telHrefMixin'

export default {
  name: 'CsdPageFooter',
  mixins: [telHrefMixin]
}
</script>
