// This is the main.js file. Import global CSS and scripts here.
// The Client API can be used here. Learn more: gridsome.org/docs/client-api

import DefaultLayout from '~/layouts/Default.vue'
import './assets/scss/main.scss'

export default function (Vue, { router, head, isClient }) {
  // Set default layout as a global component
  Vue.component('Layout', DefaultLayout)
  head.htmlAttrs = { lang: 'ru' }
  head.meta.push({
    name: 'viewport',
    content: 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no'
  })
  head.link.push({
    rel: 'preconnect',
    href: 'https://fonts.googleapis.com'
  })
  head.link.push({
    rel: 'preconnect',
    href: 'https://fonts.gstatic.com',
    crossOrigin: true
  })
  head.link.push({
    rel: 'apple-touch-icon',
    href: '/apple-touch-icon.png',
    sizes: '180x180'
  })
  head.link.push({
    rel: 'icon',
    type: 'image/png',
    sizes: '32x32',
    href: '/favicon-32x32.png'
  })
  head.link.push({
    rel: 'icon',
    type: 'image/png',
    sizes: '16x16',
    href: '/favicon-16x16.png'
  })
  head.link.push({
    rel: 'manifest',
    href: '/site.webmanifest'
  })
}
