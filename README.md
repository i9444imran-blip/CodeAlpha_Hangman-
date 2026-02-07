# 🪢 Hangman Game (Python Tkinter)

A fun **Hangman game** built using **Python** and **Tkinter** with a graphical user interface. The game includes word clues, scoring, hints, and a visual hangman drawing that updates with each wrong guess.

---

## 🎮 Features

* 🖥️ Interactive **GUI using Tkinter**
* 🔤 On-screen alphabet buttons
* 💡 Clue provided for every word
* 🧠 **Hint system** (reveals a letter with a score penalty)
* 🎯 Scoring system:

  * +10 points for correct guesses
  * −5 points for wrong guesses
  * −20 points for using a hint
  * +100 bonus for winning
* 🎨 Visual hangman drawing that updates step by step
* 🔄 New Game option

---

## 📸 Preview

> The game window displays:
>
> * Hangman drawing area
> * Hidden word with blanks
> * Clue text
> * Letter buttons (A–Z)
> * Score and game status

---

## 🛠️ Requirements

* Python **3.x**
* Tkinter (comes pre-installed with most Python distributions)

To check if Tkinter is installed:

```bash
python -m tkinter
```

---

## ▶️ How to Run

1. Clone this repository or download the file:

   ```bash
   git clone https://github.com/your-username/hangman-game.git
   ```

2. Navigate to the project folder:

   ```bash
   cd hangman-game
   ```

3. Run the game:

   ```bash
   python Hangman-Game.py
   ```

---

## 📁 Project Structure

```
Hangman-Game.py   # Main game file
README.md         # Project documentation
```

---

## 🧩 Game Logic Overview

* A random word is selected from a predefined list
* Each word has a matching clue
* The player clicks letters to guess the word
* Wrong guesses draw parts of the hangman (max 6)
* The game ends when:

  * ✅ All letters are guessed (Win)
  * ❌ Maximum wrong guesses reached (Lose)

---

## 🚀 Future Improvements (Ideas)

* Add difficulty levels
* Load words from an external file
* Add sound effects
* Add timer-based gameplay
* Save high scores
