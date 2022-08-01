// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api/

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`
const axios = require('axios')
const { createProxyMiddleware } = require('http-proxy-middleware')

const server = `${process.env.GRIDSOME_API_URL}`
const urls = {
  news: `${server}/news`,
  clients: `${server}/clients`,
  regions: `${server}/main/contacts`,
  hero: `${server}/main/title`,
  services: `${server}/services`,
  accreditationInfo: `${server}/accreditation/info`,
  accreditationCertificates: `${server}/accreditation/certificates`
}

module.exports = async function (api) {
  api.configureServer(app => {
    app.use(createProxyMiddleware('/api/v1', {
      // if you have a .env file, set this variable to something like http://localhost:1337 (I used Strapi)
      target: 'http://yarlikvid.ru:8000',
      changeOrigin: true
    }))
  })

  api.loadSource(async (actions) => {
    const addresses = actions.addCollection({ typeName: 'Addresses' })
    const _addresses = await axios.get(urls.regions)
    _addresses.data.forEach((address) => addresses.addNode(address))


    const services = actions.addCollection({ typeName: 'Services' })
    const _services = await axios.get(urls.services)
    _services.data.forEach((service) => services.addNode(service))

    const clients = actions.addCollection({ typeName: 'Clients' })
    const _clients = await axios.get(urls.clients)
    _clients.data.forEach((client) => clients.addNode(client))

    const certificates = actions.addCollection({ typeName: 'Certificates' })
    const _certificates = await axios.get(urls.accreditationCertificates)
    _certificates.data.forEach((cert) => certificates.addNode(cert))

    const news = actions.addCollection({ typeName: 'News' })
    const _news = await axios.get(urls.news)
    for (const datum of _news.data) {
      const fullNews = await axios.get(`${urls.news}/${datum.id}`)
      const result = { ...fullNews.data, short_text: datum.text }
      news.addNode(result)
    }

    const hero = actions.addCollection({ typeName: 'Hero' })
    const _hero = await axios.get(urls.hero)
    hero.addNode({ id: 1, ..._hero.data })

    const _requisites = actions.addCollection({ typeName: 'Requisites' })
    _requisites.addNode({
      id: '1',
      name: 'ООО «ЦСД»',
      inn: '6195000755',
      ogrn: '1196196007501'
    })

    const accreditationInfo = actions.addCollection({ typeName: 'AccreditationInfo' })
    const _accreditationInfo = await axios.get(urls.accreditationInfo)
    accreditationInfo.addNode({ id: 1, ..._accreditationInfo.data })
  })

  api.createPages(async ({ graphql, createPage }) => {
    const { data } = await graphql(`{
        allServices {
          edges {
            node {
              id  
            }
          }
        }
      }`)
    for (const { node } of data.allServices.edges) {
      createPage({
        path: `/services/${node.id}`,
        component: './src/pages/services/[id].vue',
        context: {
          serviceId: node.id
        }
      })
    }
  })

  api.createPages(async ({ graphql, createPage }) => {
    const { data } = await graphql(`{
        allNews {
          edges {
            node {
              id  
            }
          }
        }
      }`)
    for (const { node } of data.allNews.edges) {
      createPage({
        path: `/news/${node.id}`,
        component: './src/pages/news/[id].vue',
        context: {
          newsId: node.id
        }
      })
    }
  })
}
