<template>
  <nav class="navigation">
    <ul class="menu">
      <li
        class="menu__item"
        @click="submenu ? menuItemHover = !menuItemHover : ''"
        v-for="{to, name, submenu} in menu">
        <g-link
          :to="to"
          v-if="!submenu"
          class="menu__link"
          exact-active-class="menu__link_active"
          active-class="menu__link_active'">
          {{ name }}
        </g-link>
        <g-link
          v-else
          :to="to"
          event=""
          class="menu__link"
          exact-active-class="menu__link_active"
          :active-class="submenu ? 'menu__link_active' : ''">
          {{ name }}
          <template v-if="submenu">
            <icon-arrow-down/>
          </template>
        </g-link>
        <template v-if="submenu">
          <ul :class="['submenu', {'submenu_visible': menuItemHover}]">
            <li
              v-for="{node} in $static[submenu].edges"
              class="submenu__item">
              <g-link
                class="submenu__link"
                :to="`/services/${node.id}`"
              >{{ node.title }}
              </g-link>
            </li>
          </ul>
        </template>
      </li>
    </ul>
  </nav>
</template>
<static-query>
query {
  allServices {
    edges {
      node {
        id
        title
      }
    }
  }
}
</static-query>
<script>
import IconArrowDown from './icons/IconArrowDown'

export default {
  name: 'CsdNavigation',
  components: { IconArrowDown },
  data() {
    return {
      menuItemHover: false,
      menu: [
        {
          to: '/',
          name: 'Главная'
        },
        {
          to: '/#about',
          name: 'О компании'
        },
        {
          to: '/services',
          name: 'Услуги',
          clickable: false,
          submenu: 'allServices'
        },
        {
          to: '/prices',
          name: 'Цены'
        },
        {
          to: '/#clients',
          name: 'Наши клиенты'
        },
        {
          to: '/contacts',
          name: 'Контакты'
        }
      ]
    }
  }
}
</script>

<style lang="scss">

</style>