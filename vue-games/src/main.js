import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'

import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)
/*
Vue 3:
const app = Vue.createApp(...)
app.use(VueAxios, axios)
*/
/*
https://stackoverflow.com/questions/48650107/use-axios-globally-in-all-my-components-vue
import Axios from 'axios'
Vue.prototype.$http = Axios;
*/
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
