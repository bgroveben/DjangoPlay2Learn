<template>
  <!--<div class="row mx-1 my-3">-->
    <div class="row mx-auto my-3">
    <label :for="id" class="col font-weight-bold text-center fs-5">{{label}}</label>
    <select class="col form-control" :id="id" :value="currentValue"
        @input="$emit('input', $event.target.value)">
      <option v-for="option in options" :key="option[1]"
        :value="option[1]">
        {{option[0]}}
      </option>
    </select>
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script>
  export default {
    name: 'SelectInput',
    props: {
      id: String,
      label: String,
      options: Array,
      currentValue: String
    }
  }
</script>