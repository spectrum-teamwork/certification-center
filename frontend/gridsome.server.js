// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api/

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`
const axios = require('axios')
const { createProxyMiddleware } = require('http-proxy-middleware')

const server = `http://yarlikvid.ru:8000/api/v1`
const urls = {
  news: `${server}/news`,
  clients: `${server}/clients`,
  regions: `${server}/main/contacts`,
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
    const _news = [
      {
        id: '0',
        image: '/assets/img/news/1.png',
        heading: 'Приняты изменения в ТР ТС 004/2011 и 020/2011',
        highlight: 'На заседании Совета ЕЭК 10 июня приняты решения о внесении изменений в технические регламент'
      },
      {
        id: '1',
        image: '/assets/img/news/2.png',
        heading: 'О временных дополнениях в типовые схемы оценки',
        highlight: 'Коллегия ЕЭК приняла Распоряжение №67 от 26 апреля 2022 года, которым утверждается'
      },
      {
        id: '2',
        image: '/assets/img/news/3.png',
        heading: 'Проект изменений №2 в ТР ТС 019/2011',
        highlight: 'На Правовом портале Евразийского экономического союза размещён для общественного обсуждения проект'
      },
      {
        id: '3',
        image: '/assets/img/news/4.png',
        heading: 'Обсуждение проекта изменений в ТР ТС 019/2011',
        highlight: 'С 1 мая 2022 года начнется процедура общественного обсуждения проекта изменений в ТР ТС 019/2011'
      }
    ]
    _news.forEach((event) => news.addNode(event))

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
}
