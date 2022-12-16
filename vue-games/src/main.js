import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'

import axios from 'axios'
import VueAxios from 'vue-axios' // Do I need this?
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
Vue.use(VueAxios, axios)

Vue.use(VueRouter)
import About from './components/About.vue'
import Login from './components/Login.vue'
import Contact from './components/Contact.vue'
import Home from './components/Home.vue'
import MathFacts from './components/MathFacts.vue'
import AnagramHunt from './components/AnagramHunt.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About },
  { path: '/login', component: Login },
  { path: '/contact', component: Contact },
  { path: '/games/math-facts', component: MathFacts },
  { path: '/games/anagram-hunt', component: AnagramHunt },
]
const router = new VueRouter({
  routes
})
Vue.config.productionTip = false
new Vue({
  render: h => h(App),
  router
}).$mount('#app')
