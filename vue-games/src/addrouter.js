//import { createWebHistory, createRouter } from "vue-router";
import Router from 'vue-router'
//import AnagramHunt from '.components/AnagramHunt.vue';
//import MathFacts from '.components/MathFacts.vue';

import MathFacts from './components/MathFacts.vue'
import AnagramHunt from './components/AnagramHunt.vue'

const routes = [
  {
    path: '/anagram-hunt',
    component: AnagramHunt
  },
  {
    path: '/math-facts',
    component: MathFacts
  },
];

// const addrouter = createRouter({
const addrouter = new Router({
  //history: createWebHistory(),
  routes: routes,
});

export default addrouter;
