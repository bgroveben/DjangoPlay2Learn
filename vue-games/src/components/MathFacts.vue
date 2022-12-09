<template>
  <main id="main-container">
    <div v-if="screen === 'config'" id="config-container" class="col-5 mx-auto">
      <h1 class="text-center mb-3">Math Facts</h1>
      <SelectInput :currentValue="operation" label="Choose Operation"
        id="operation" v-model="operation" :options="operations" />
      <SelectInput :currentValue="maxNumber" label="Choose Max Number"
        id="max-number" v-model="maxNumber" :options="numbers" />
      <SelectInput :currentValue="gameLength.toString()" label="Choose Game Length"
        id="game-length" v-model="gameLength" :options="times" />
      <PlayButton @play-button-click="play" />
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
              <div class="col px-3 text-left fs-2">
                <Score :score="score" />
              </div>
              <div class="col px-3 text-right fs-2">
                <Timer :timeLeft="parseInt(timeLeft)" />
              </div>
            </div>
            <div :class="equationClass" id="equation">
              <Equation :question="question"
                :answer="input"
                :answered="answered" />
            </div>
            <div class="row" id="buttons">
              <div class="col-3 mx-auto w-auto mt-2">
                <button class="btn btn-primary bg-gradient col-4 p-1 border border-dark border-4 rounded-circle fs-2"
                  v-for="button in buttons" :key="button"
                  @click="setInput(button)">{{button}}</button>
                <button class="btn btn-primary bg-gradient col-8 p-1 border border-dark border-4 rounded-circle fs-2" id="clear-button"
                  @click="clear">CLEAR</button>
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
  import Score from './Score';
  import Timer from './Timer';
  import Equation from './Equation';
  import {randInt} from '../helpers/helpers';
  export default {
    name: 'Main',
    components: {
      SelectInput,
      PlayButton,
      Score,
      Timer,
      Equation
    },
    data: function() {
      return {
        operations: [
          ['Addition', '+'],
          ['Subtraction', '-'],
          ['Multiplication', 'x'],
          ['Division', '/']
        ],
        operation: 'x',
        maxNumber: '10',
        buttons: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        screen: 'config',
        input: '',
        operands: {num1: '1', num2: '1'},
        answered: false,
        score: 0,
        gameLength: 60,
        timeLeft: 0
      }
    },
    methods: {
      config() {
        this.screen = "config";
      },
      play() {
        this.screen = "play";
        this.newQuestion();
        this.startTimer();
      },
      setInput(value) {
        this.input += String(value);
        this.input = String(Number(this.input));
        this.answered = this.checkAnswer(this.input,
                                        this.operation,
                                        this.operands);
        if (this.answered) {
          setTimeout(this.newQuestion, 300);
          this.score++;
        }
      },
      clear() {
        this.input = '';
      },
      getRandNumbers(operator, low, high) {
        let num1 = randInt(low, high);
        let num2 = randInt(low, high);
        const numHigh = Math.max(num1, num2);
        const numLow = Math.min(num1, num2);

        if(operator === '-') { // Make sure higher num comes first
          num1 = numHigh;
          num2 = numLow;
        }

        if(operator === '/') {
          if (num2 === 0) { // No division by zero
            num2 = randInt(1, high);
          }
          num1 = (num1 * num2);
        }
        return {num1, num2};
      },
      checkAnswer(userAnswer, operation, operands) {
        if (isNaN(userAnswer)) return false; // User hasn't answered

        let correctAnswer;
        switch(operation) {
          case '+':
            correctAnswer = operands.num1 + operands.num2;
            break;
          case '-':
            correctAnswer = operands.num1 - operands.num2;
            break;
          case 'x':
            correctAnswer = operands.num1 * operands.num2;
            break;
          default: // division
            correctAnswer = operands.num1 / operands.num2;
        }
        return (parseInt(userAnswer) === correctAnswer);
      },
      newQuestion() {
        this.input='';
        this.answered = false;
        this.operands = this.getRandNumbers(
          this.operation, 0, this.maxNumber
        );
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
        this.startTimer();
        this.newQuestion();
      },
      handleKeyUp(e) {
        e.preventDefault(); // prevent the normal behavior of the key
        if (e.keyCode === 32 || e.keyCode === 13) { // space/Enter
          this.clear();
        } else if (e.keyCode === 8) { // backspace
          this.input = this.input.substring(0, this.input.length - 1);
        } else if (!isNaN(e.key)) {
          this.setInput(e.key);
        }
      }
    },
    computed: {
      numbers: function() {
        const numbers = [];
        for (let number = 2; number <= 100; number++) {
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
      },
      question: function() {
        const num1 = this.operands.num1;
        const num2 = this.operands.num2;
        const equation = `${num1} ${this.operation} ${num2}`;
        return equation;
      },
      equationClass: function() {
        if (this.answered) {
          return 'row text-primary my-2 fade';
        } else {
          return 'row text-secondary my-2';
        }
      }
    }
  }
</script>

