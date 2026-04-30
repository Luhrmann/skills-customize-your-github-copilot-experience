
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman word-guessing game using Python to practice string manipulation, loops, conditionals, and user input. Implement core game logic, track guesses, and display game state clearly to the player.

## 📝 Tasks

### 🛠️ Game Mechanics and Word Selection

#### Description
Implement the core Hangman mechanics: select a random word from a list, accept letter guesses, and reveal correctly guessed letters.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept single-letter guesses from the user (case-insensitive)
- Reveal correctly guessed letters in the word display (e.g., `_ a _ g _ a _`)
- Prevent counting repeated correct guesses as additional wrong attempts


### 🛠️ Win/Loss Conditions and User Interface

#### Description
Track incorrect guesses and implement win/lose conditions with clear user prompts and status updates after each guess.

#### Requirements
Completed program should:

- Track and display remaining incorrect attempts (for example, 6 attempts)
- End the game when the user guesses the word or uses all attempts
- Display a clear win message showing the completed word or a lose message revealing the correct word
- Show current progress and list incorrect guesses after each turn

Example interaction:

```
Welcome to Hangman!
_ _ _ _ _ _
Guess a letter: a
_ a _ _ _ _
Incorrect guesses: []
Remaining attempts: 6
Guess a letter: e
_ a _ _ _ _
Incorrect guesses: ['e']
Remaining attempts: 5
```

