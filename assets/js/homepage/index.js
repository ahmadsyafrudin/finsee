import App from '../../riot/app.riot';
import Header from '../../riot/navbar.riot';
import Banner from '../../riot/banner.riot';

const riot = require('riot');

const mountApp = riot.component(App)
const headerApp = riot.component(Header)
const bannerApp = riot.component(Banner)

const app = mountApp(
  document.getElementById('root'),
  {
          title: 'I want to behave!',
          items: [
            { title: 'Avoid excessive caffeine', done: true },
            { title: 'Hidden item',  hidden: true },
            { title: 'Be less provocative'  },
            { title: 'Be nice to people' }
          ]
        }
)

const header = headerApp(
    document.getElementById("navbar-header"),
    {"user": "Rudi"}
)

const banner = bannerApp(
    document.getElementById("banner"),
    {"app_name": "Finsee"}
)
