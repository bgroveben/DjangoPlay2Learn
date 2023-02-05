<template>
    <main class="bg-secondary bg-gradient bg-opacity-10">
        <section class="row pb-4" id="gamessection">
            <article class="col-sm col-md border rounded-3 border-warning mx-4 bg-primary bg-gradient" id="article1">
                <h2 class="text-light">Math Facts</h2>
                <p class="text-light">This is a simple game for practicing addition, subtraction, multiplication, and division. The equation appears with a text field below it. Enter values using the keyboard or the buttons on the screen, and solve the problems.</p>
                <button class="btn btn-warning mb-2"><router-link to="/games/math-facts" class="nav-link mx-3 h3">Play Now!</router-link></button>
            </article>

            <article class="col-sm col-md border rounded-3 border-warning mx-4 bg-primary bg-gradient" id="article2">
                <h2 class="text-light">Anagram Hunt</h2>
                <p class="text-light">An anagram is a word made by rearranging the letters of another word. For example, post, pots, opts, tops, and spot are all anagrams of stop. The object of the Anagram Hunt game is to find all the anagrams for a given word.</p>
                <button class="btn btn-warning mb-2"><router-link to="/games/anagram-hunt" class="nav-link mx-3 h3">Play Now!</router-link></button>
            </article>
        </section>
    </main>
</template>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

<script>
  export default {
    name: 'Home',
  }
</script>
