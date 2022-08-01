<template>
  <form class="price-calc-form" @submit.prevent="onFormSubmit">
    <div class="price-calc-form__heading">
      Рассчитать стоимость
    </div>
    <select required v-model="form.service_id" v-if="$context.serviceId === undefined">
      <option disabled hidden selected value="7334d757-3fae-4b38-8e54-892007162adf">Выберите услугу из списка</option>
      <option
        :value="node.id"
        v-model="form.serviceId"
        v-for="{node} in $static.allServices.edges">
        {{ node.title }}
      </option>
    </select>
    <input v-else ref="serviceIdInput" type="text" hidden :value="$context.serviceId">
    <input
      required
      type="text"
      name="fullname"
      placeholder="Имя"
      v-model="form.contact_name"
      class="price-calc-form__input-name"
    >
    <input
      type="tel"
      name="tel"
      v-model="form.phone"
      placeholder="Номер телефона"
      class="price-calc-form__input-tel"
    >
    <button :class="['price-calc-form__button', submitButtonClasses]">{{ submitButtonText }}</button>
  </form>
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
import createOrder from '../mixins/createOrder'
import onRegionUpdate from '../mixins/onRegionUpdate'
import Cookies from 'js-cookie'

export default {
  name: 'CsdPriceCalcForm',
  mixins: [createOrder, onRegionUpdate],
  data() {
    return {
      submitButtonTimeout: null,
      submitButtonText: 'Отправить',
      submitButtonClasses: {
        'price-calc-form__button_error': false,
        'price-calc-form__button_success': false
      },
      form: {
        contact_id: '',
        service_id: '7334d757-3fae-4b38-8e54-892007162adf',
        contact_name: '',
        phone: ''
      }
    }
  },
  methods: {
    async onFormSubmit() {
      this.resetSubmitButton()
      this.form.contact_id = Cookies.get('_region')
      await this.createOrder(this.form)
    },
    resetSubmitButton(timeout = 0) {
      clearTimeout(this.submitButtonTimeout)
      this.submitButtonTimeout = setTimeout(() => {
        this.submitButtonText = 'Отправить'
        this.submitButtonClasses['price-calc-form__button_error'] = false
        this.submitButtonClasses['price-calc-form__button_success'] = false
      }, timeout)
    }
  },
  watch: {
    'createOrderState.success': {
      handler(status) {
        if (status) {
          this.submitButtonText = 'Отправлено'
          this.submitButtonClasses['price-calc-form__button_success'] = true
          this.resetSubmitButton(1500)
        }
      }
    },
    'createOrderState.error': {
      handler(status) {
        if (status) {
          this.submitButtonText = 'Ошибка'
          this.submitButtonClasses['price-calc-form__button_error'] = true
          this.resetSubmitButton(1500)
        }
      }
    }
  },
  mounted() {
    addEventListener('onregionupdate', (event) => {
      this.form.contact_id = event.detail.regionId
    })
    if (this.$refs?.serviceIdInput) {
      this.form.service_id = this.$refs.serviceIdInput.value
    }
  }
}
</script>
