<template>
  <div id="equation" class="row display-4">
    <div class="col-6 text-end">{{question}}</div>
    <div class="col-1">=</div>
    <div class="col-4 text-start">{{answer}}</div>
  </div>
</template>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

<script>
  export default {
    name: 'Equation',
    props: {
      question: String,
      answer: String,
      answered: Boolean
    }
  }
</script>