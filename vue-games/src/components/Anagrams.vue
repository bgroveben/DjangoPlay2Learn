<template>
  <div id="body">
    <div>
        <div class="row">
            <h4 class="text-danger">Remaining: {{anagramsLeft}}</h4>
          <div class="row mt-1">
            <h2 class="text-secondary">Guessed: {{anagramsGuessed.toString()}}</h2>
          </div>
        </div>
    </div>   
  </div>
</template>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script>
export default {
    name: 'Anagrams',
    props: {
        anagramsGuessed: Array, // Correct answers by user
        anagramsLeft: Number // Number of words left in anagram's array
    }
  }
</script>