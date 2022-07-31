// This is where project configuration and plugin options are located.
// Learn more: https://gridsome.org/docs/config

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const server = `http://yarlikvid.ru:8000/api/v1`
const urls = {
  news: `${server}/news`,
  clients: `${server}/clients`,
  regions: `${server}/contacts`,
  services: `${server}/services`,
  accreditationInfo: `${server}/accreditation/info`,
  accreditationCertificates: `${server}/accreditation/certificates`
}

module.exports = {
  siteName: 'ЦСД - Центр сертификации и декларирования',
  plugins: [
    {
      use: '@gridsome/plugin-critical',
      options: {
        paths: ['/', '/about', '/clients', '/contacts', '/news', '/prices'],
        width: 320,
        height: 640
      }
    }
  ]
}
