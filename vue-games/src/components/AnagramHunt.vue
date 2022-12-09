<template>
  <main id="main-container">
    <div v-if="screen === 'config'" id="config-container" class="col-5 mx-auto">
      <h1 class="text-center mb-2">Anagram Hunt</h1>
      <SelectInput :currentValue="maxNumber" label="Choose Word Length"
        id="max-number" v-model="maxNumber" :options="numbers" />
      <SelectInput :currentValue="gameLength.toString()" label="Choose Game Length"
        id="game-length" v-model="gameLength" :options="times" />
      <PlayButton @play-button-click="play" />
      <div class="text-center">
        <small class="text-muted">anagrams courtesy of enchantedlearning.com</small>
      </div>
    </div>
    <div v-else-if="screen === 'play'" id="game-container" class="text-center">
      <transition name="slide">
        <template v-if="timeLeft === 0">
          <div>
            <h2 class="fs-1">Time's Up!</h2>
            <strong class="h3">You Answered</strong>
            <div class="display-2">{{score}}</div>
            <strong class="h3">Questions Correctly</strong>
            <button class="btn btn-success col-3 mx-auto d-grid gap-2 my-3 p-2 fs-5 rounded-circle"
              v-on:click="restart()">
                Play Again
            </button>
            <button class="btn btn-danger col-3 mx-auto d-grid gap-2 my-3 p-2 fs-5 rounded-circle"
              v-on:click="config()">
                Change Settings
            </button>
          </div>
        </template>
      </transition>
      <transition name="slide-right">
        <template v-if="timeLeft > 0">
          <div class="w-50 mx-auto">
            <div class="row border-bottom" id="scoreboard">
              <div class="col px-3 fs-2">
                <Score :score="score" />
              </div>
              <div class="col px-3 fs-2">
                <Timer :timeLeft="parseInt(timeLeft)" />
              </div>
            </div>
            <div class="row border-bottom">
              <div class="col text-center mt-2">
                <h2 class="fw-bold text-primary fs-1" id="anagram">{{anagram}}</h2>
                <h2 class="fw-bold text-secondary fs-1" id="answer">{{answer}}</h2>
                <div>
                  <div class="my-3">
                    <input type="text" class="col-6 fs-4 form-control-lg" v-model="answer" ref="answer" placeholder="Answer" aria-label="Answer" id="answer" aria-describedby="Answer" />
                  </div>
                </div>
                <InputButton @is-anagram="isAnagram" />
                <Anagrams :anagramsGuessed="anagramsGuessed" :anagramsLeft="anagramsLeft" />
              </div>
            </div>
          </div>
        </template>
      </transition>
    </div>
  </main>
</template>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

<script>
  import SelectInput from './SelectInput';
  import PlayButton from './PlayButton';
  import InputButton from './InputButton.vue';
  import Score from './Score';
  import Timer from './Timer';
  import Anagrams from './Anagrams';
  import anagrams from "../../src/helpers/anagrams.js";
  import {randInt} from '../helpers/gameplay.js';
  export default {
    name: 'Main',
    components: {
      SelectInput,
      PlayButton,
      Score,
      Timer,
      Anagrams,
      InputButton
    },
    data: function() {
      return {
        operations: [
          ['5'],['6'],['7'],['8']
        ],
        screen: 'config',
        input: '',
        maxNumber: '5',
        anagrams: anagrams,
        outerArray: [1],
        randomOuter: [1],
        anagram: [],
        answer: '',
        anagramsLeft: [],
        anagramsGuessed: [],
        answered: false,
        score: 0,
        gameLength: 60,
        timeLeft: 0
      }
    },
    methods: {
      chooseAnagram() {
        if (this.outerArray.length === 0 && this.randomOuter.length === 0) {
          // this.self.patOnBack();
          console.log("********** WINNER *********");
          this.anagrams = {};
          this.randomOuter = [1];
          this.anagram = 'You Guessed All Of Them!';
          return true;  // Game over, stop the rest of the function
        }
        this.chooseWordLength();
        this.answer = '';
        this.$nextTick(() => this.$refs.answer.focus());
        // remove sub-array from outer array
        this.outerArray.splice(this.outerArray.indexOf(this.randomOuter), 1); 
        this.anagramsGuessed = [];
         // remove displayed anagram from array
        this.randomOuter.splice(this.randomOuter.indexOf(this.anagram), 1);
        this.anagramsLeft = this.randomOuter.length;
        // cheating => display remaining anagrams in console;
        // enabled by default
        console.log("cheating: " + this.randomOuter);
        // if you think you need a cheating function for the MathFacts game, think harder
      },
      isAnagram() {
        this.answer = this.answer.toLowerCase();
        if (this.randomOuter.includes(this.answer)) {
          this.anagramsGuessed.push(this.answer);
          // remove chosen answer from array 
          this.randomOuter.splice(this.randomOuter.indexOf(this.answer), 1); 
          this.score++;
          this.answer = '';
          this.$nextTick(() => this.$refs.answer.focus());
          this.anagramsLeft -= 1;
          // cheating()
          console.log("cheating: " + this.randomOuter);
        }
        if (this.randomOuter.length < 1) {
          this.chooseAnagram();
          this.answer = '';
          this.$nextTick(() => this.$refs.answer.focus());
          this.anagramsGuessed = [];
        }
          this.answer = '';
          this.$nextTick(() => this.$refs.answer.focus());
      },
      config() {
        this.screen = "config";
      },
      chooseWordLength() {
        switch (this.maxNumber) {
          case '5':
            this.outerArray = Object.values(this.anagrams)[0]
            this.randomOuter = this.outerArray[randInt(0, this.outerArray.length-1)];
            this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
            break;
          case '6':
            this.outerArray = Object.values(this.anagrams)[1];
            this.randomOuter = this.outerArray[randInt(0, this.outerArray.length-1)];
            this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
            break;
          case '7':
            this.outerArray = Object.values(this.anagrams)[2];
            this.randomOuter = this.outerArray[randInt(0, this.outerArray.length-1)];
            this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
            break;
          case '8':
            this.outerArray = Object.values(this.anagrams)[3]
            this.randomOuter = this.outerArray[randInt(0, this.outerArray.length-1)];
            this.anagram = this.randomOuter[randInt(0, this.randomOuter.length-1)];
            break;
        } // You don't need a default statement
      },
      play() {
        this.score = 0;
        this.screen = "play";
        this.startTimer();
        this.$nextTick(() => this.$refs.answer.focus());
         // Deep Copy
        this.anagrams = JSON.parse(JSON.stringify(Object.values(anagrams)));
        this.chooseAnagram();
      },
      clear() {
        this.input = '';
      },
 
      startTimer() {
        window.addEventListener('keyup', this.handleKeyUp);
        this.timeLeft = this.gameLength;
        if (this.timeLeft > 0) {
          this.timer = setInterval(() => {
            this.timeLeft--;
            if (this.timeLeft === 0) {
              clearInterval(this.timer);
              window.removeEventListener('keyup', this.handleKeyUp);
            }
          }, 1000)
        }
      },
      restart() {
        this.score = 0;
         // Deep Copy
        this.anagrams = JSON.parse(JSON.stringify(Object.values(anagrams)));
        this.chooseAnagram();
        this.startTimer();
      },
    },
    computed: {
      numbers: function() {
        const numbers = [];
        for (let number = 5; number <= 8; number++) {
          numbers.push([number, number]);
        }
        return numbers;
      },
      times: function() {
        const times = [];
        for (let time = 30; time <= 120; time+=30) {
          times.push([time.toString(), time.toString()]);
        }
        return times;
      }
    }
  }
</script>
