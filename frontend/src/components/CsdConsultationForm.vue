<template>
  <div class="leave-order-form">
    <div class="container-fluid px-0">
      <div class="row">
        <div :class="{'col-10':closeable, 'col-12': !closeable}">
          <span class="leave-order-form__heading">
            Оставьте заявку
          </span>
        </div>
        <div class="col-2" v-if="closeable">
          <button class="ml-auto mt-md-3 button_modal-close" @click="$emit('close')">
            <icon-close/>
          </button>
        </div>
      </div>
    </div>
    <form class="form" @submit.prevent="onFormSubmit">
      <div class="container-fluid px-0">
        <div class="row">
          <div class="col-12 col-sm-6">
            <input
              required
              v-model="form.contact_name"
              name="fullname"
              type="text"
              placeholder="Ваше имя">
          </div>
          <div class="col-12 col-sm-6">
            <input
              required
              name="tel"
              type="tel"
              v-model="form.phone"
              placeholder="Номер телефона">
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <textarea
              name="comment"
              v-model="form.comment"
              placeholder="Ваш вопрос"/>
          </div>
        </div>
        <div class="row mt-4 mt-lg-0">
          <div class="col-12 col-lg-8">
            <div class="checkbox-field">
              <input v-model="form.agree" required id="agree" type="checkbox">
              <label for="agree">Я согласен на обработку персональных данных</label>
            </div>
          </div>
          <div class="col-12 col-lg-4">
            <csd-button
              type="submit"
              :loading="createOrderState.loading"
              :class="[
                submitButtonClasses,
                'button-submit ml-lg-auto mt-4 mt-lg-0'
                ]"
              :label="submitButtonText"
            />
          </div>
        </div>
      </div>
    </form>
  </div>
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
import Cookies from 'js-cookie'
import IconClose from './icons/IconClose'
import CsdButton from './CsdButton'
import createOrder from '../mixins/createOrder'
import onRegionUpdate from '../mixins/onRegionUpdate'

export default {
  name: 'CsdConsultationForm',
  components: { CsdButton, IconClose },
  mixins: [createOrder, onRegionUpdate],
  props: {
    closeable: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      submitButtonTimeout: null,
      submitButtonText: 'Отправить',
      submitButtonClasses: {
        button_error: false,
        button_success: false
      },
      form: {
        contact_id: '',
        contact_name: '',
        phone: '',
        comment: '',
        agree: false
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
        this.submitButtonClasses.button_error = false
        this.submitButtonClasses.button_success = false
      }, timeout)
    }
  },
  watch: {
    'createOrderState.success': {
      handler(status) {
        if (status) {
          this.submitButtonText = 'Отправлено'
          this.submitButtonClasses.button_success = true
          this.resetSubmitButton(1500)
        }
      }
    },
    'createOrderState.error': {
      handler(status) {
        if (status) {
          this.submitButtonText = 'Ошибка'
          this.submitButtonClasses.button_error = true
          this.resetSubmitButton(1500)
        }
      }
    }
  },
  mounted() {
    addEventListener('onregionupdate', (event) => {
      this.form.contact_id = event.detail.regionId
    })
  }
}
</script>
