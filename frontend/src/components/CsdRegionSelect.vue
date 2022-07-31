<template>
  <div class="region" :key="currentRegionId" v-if="setRegionsList($static.allAddresses.edges)">
    <div class="region__link">
      <span
        class="link__text">
        {{ currentRegionName }}
      </span>
      <div class="dropdown-arrow">
        <icon-arrow-down/>
      </div>
    </div>
    <ul class="region__list">
      <template v-for="({node}, index) in regionsListOrder">
        <li
          @click="setRegion(node.id)"
          :class="['region__item', {'region__link': node.id === currentRegionId}]"
        >
          <span class="link__text">{{ node.region }}</span>
          <div v-if="node.id === currentRegionId" class="dropdown-arrow">
            <icon-arrow-down/>
          </div>
        </li>
        <li
          class="region__divider"
          v-if="index !== regionsListOrder.length - 1"
        />
      </template>
    </ul>
  </div>
</template>
<static-query>
query addresses {
  allAddresses {
    edges {
      node {
        id
        region
      }
    }
  }
}
</static-query>
<script>
import Cookies from 'js-cookie'
import IconArrowDown from './icons/IconArrowDown'

export default {
  components: { IconArrowDown },
  data() {
    return {
      regionsList: [],
      currentRegionId: undefined,
      defaultRegionIndex: 0
    }
  },
  methods: {
    setDefaultRegion(regions) {
      if (this.currentRegionId === undefined) {
        this.setRegion(regions[this.defaultRegionIndex].node.id)
      }
      return true
    },
    setRegionsList(regions) {
      this.regionsList = regions
      this.setDefaultRegion(this.regionsList)
      return true
    },
    setRegion(regionId) {
      Cookies.set('_region', regionId)
      this.currentRegionId = regionId
    }
  },
  computed: {
    currentRegionName() {
      const r = this.regionsList.find((edge) => {
        return edge.node.id === this.currentRegionId
      })
      return r.node.region
    },
    regionsListOrder() {
      if (this.currentRegionId === undefined) {
        return this.regionsList
      }
      const result = this.regionsList.filter((edge) => edge.node.id !== this.currentRegionId)
      result.unshift(this.regionsList.find((edge) => edge.node.id === this.currentRegionId))
      return result
    }
  },
  watch: {
    currentRegionId: {
      handler(regionId) {
        dispatchEvent(new CustomEvent('onregionupdate', {
          detail: { regionId }
        }))
      }
    }
  },
  beforeMount() {
    this.currentRegionId = Cookies.get('_region')
  }
}
</script>