import axios from 'axios'

const STATUS = {
  LOADING: Symbol('PENDING'),
  FAILED: Symbol('FAILED'),
  SUCCESS: Symbol('SUCCESS')
}
export default {
  data() {
    return {
      createOrderState: {
        loading: false,
        failed: false,
        success: false,
        error: undefined,
        data: undefined
      }
    }
  },
  methods: {
    setCreateOrderState(status, state = { response: undefined, error: undefined }) {
      this.createOrderState.loading = status === STATUS.LOADING
      this.createOrderState.failed = status === STATUS.FAILED
      this.createOrderState.success = status === STATUS.SUCCESS
      this.createOrderState.data = state?.response
      this.createOrderState.error = state?.error

    },
    async createOrder(order) {
      try {
        this.setCreateOrderState(STATUS.LOADING)
        const response = await axios.post('/api/v1/orders/order', order)
        this.setCreateOrderState(STATUS.SUCCESS, { response })
      } catch (error) {
        this.setCreateOrderState(STATUS.FAILED, { error })
      }
    }
  }
}