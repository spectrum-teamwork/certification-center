<template>
  <table class="price-list-table">
    <tbody>
    <tr v-for="{node} in $static.allServices.edges">
      <td class="price-list-table__name" v-text="node.title"></td>
      <td class="price-list-table__price">от {{ node.price }} ₽</td>
      <td class="price-list-table__more">
        <g-link :to="`/services/${node.id}`">Подробнее</g-link>
      </td>
    </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name: 'CsdPriceList'
}
</script>
<static-query>
query {
  allServices {
    edges {
      node {
        id
        title
        price
      }
    }
  }
}
</static-query>
