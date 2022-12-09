<template>
  <div class="row">
    <button class="btn btn-success col-3 mx-auto d-grid gap-2 my-3 p-3 fs-5 rounded-circle" @click="$emit('is-anagram')">
      Enter
    </button>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script>
  export default {
    name: 'InputButton'
  }
</script>