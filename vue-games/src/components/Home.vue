<template>
    <main class="bg-secondary bg-gradient bg-opacity-10">
        <div class="col-md border border-success rounded-3 bg-info bg-opacity-10 bg-gradient m-3 p-3">
            <h3 id="quotestitle">Observations, Advice, and Other Quotes:</h3>
            <!--
            <section id="quotes"></section>
            -->
            <div id="quotes-carousel" class="carousel slide carousel-fade mt-4" data-bs-ride="carousel" data-bs-pause="hover" data-bs-interval="6000">
            <div class="carousel-inner">
                <div class="carousel-item active bg-success bg-opacity-10 bg-gradient">
                <h6>"We have to stop optimizing for programmers and start optimizing for users."</h6>
                <p><em>Jeff Atwood</em></p>
                </div>
                <div class="carousel-item bg-success bg-opacity-10 bg-gradient">
                <h6>"The human spirit must prevail over technology."</h6>
                <p><em>Albert Einstein</em></p>
                </div>
                <div class="carousel-item bg-success bg-opacity-10 bg-gradient">
                <h6>"Do or do not. There is no try."</h6>
                <p><em>Jedi Master Yoda</em></p>
                </div>
                <div class="carousel-item bg-success bg-opacity-10 bg-gradient">
                <h6>"Any sufficiently advanced technology is indistinguishable from magic."</h6>
                <p><em>Arthur C. Clarke</em></p>
                </div>
                <div class="carousel-item bg-success bg-opacity-10 bg-gradient">
                <h6>"The computer can't tell you the emotional story. It can give you the exact mathematical design."</h6>
                <p><em>Frank Zappa</em></p>
                </div>
                <div class="carousel-item bg-success bg-opacity-10 bg-gradient">
                <h6>"Computers are useless. They can only give you answers."</h6>
                <p><em>Pablo Picasso</em></p>
                </div>
            </div>
            </div>
        </div>

        <section class="row pb-4" id=gamessection>
            <article class="col-sm col-md border rounded-3 border-warning mx-4 bg-primary bg-gradient bg-opacity-10" id="article1">
                <h2>Math Facts</h2>
                <p>This is a simple game for practicing addition, subtraction, multiplication, and division. The equation appears with a text field below it. Enter values using the keyboard or the buttons on the screen, and solve the problems.</p>
                <button class="btn btn-warning mb-2"><router-link to="/games/math-facts" class="nav-link mx-3 h3">Play Now!</router-link></button>
            </article>

            <article class="col-sm col-md border rounded-3 border-warning mx-4 bg-primary bg-gradient bg-opacity-10" id="article2">
                <h2>Anagram Hunt</h2>
                <p>An anagram is a word made by rearranging the letters of another word. For example, post, pots, opts, tops, and spot are all anagrams of stop. The object of the Anagram Hunt game is to find all the anagrams for a given word.</p>
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