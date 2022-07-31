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
          <a href="#">Политика конфиденциальности</a>
          <a href="#">Пользовательское соглашение</a>
        </div>
        <div class="col-12 mt-4 mt-lg-0 col-lg-5 offset-lg-1 d-flex flex-column">
          Москва:
          <a :href="getTelHref('8 (800) 600-17-44')">8 (800) 600-17-44</a>
          ул. Проспект Мира, дом 39, строение 2, офис 304 БЦ Олимпик Плаза II
          <a href="mailto:krd@csd.expert">krd@csd.expert</a>
        </div>
        <div class="col-12 mt-4 mt-lg-0 col-lg-3 d-flex flex-column">
          Краснодар:
          <a :href="getTelHref('8 (800) 600-17-44')" class="text-white">8 (800) 600-17-44</a>
          ул. Адмирала Крузенштерна, дом 6
          <a href="mailto:krd@csd.expert" class="text-white">krd@csd.expert</a>
        </div>
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
}
</static-query>
<script>
import telHrefMixin from '../mixins/telHrefMixin'

export default {
  name: 'CsdPageFooter',
  mixins: [telHrefMixin]
}
</script>
