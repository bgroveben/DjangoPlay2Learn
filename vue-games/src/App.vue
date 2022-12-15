<template>
  <div id="app">{{ message }}
    <router-view/>
  </div>
</template>

<script>
/*
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data () {
    return {
      tasks: [] // Array for holding the tasks
    }
  },
  mounted () { // This will be called when HelloWorld is loaded
    this.getTasks(); // Call our getTasks function below
  },
  methods: {
    getTasks() {
        axios({
            method:'get',
            url: 'http://127.0.0.1:8000/tasks/',
            auth: {
                username: 'admin',
                password: 'password123'
            }
        }).then(response => this.tasks = response.data);
    }
  }
}
*/
export default {
  name: 'app',
  /*
  components: {
    HelloWorld,
    Header,
    Footer
  }
  */
  data(){
    return {
      message: 'Welcome to Play2Learn4Django! vue-games/src/App.vue'
    }
  }
}
</script>

<style>

</style>
