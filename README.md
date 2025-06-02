# 🕹️ Hangman Game

Welcome to the classic Hangman game, now with a fun twist! Guess the hidden word one letter at a time before the hangman is fully drawn. Can you save the day? 🕵️‍♂️

---

## ✨ Features

- 🎲 Random word selection
- ✅ Tracks correct and incorrect guesses
- 🖼️ ASCII art hangman visual
- 📝 Simple and clean terminal interface

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x 🐍

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/batmanrizz/hangman-game.git
   cd hangman-game
   ```

2. (Optional) Setup a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

### Running the Game

```bash
python hangman.py
```

---

## 🎮 How to Play

- The game selects a random word. Your goal is to guess it, one letter at a time.
- Each wrong guess draws another part of the hangman. You lose if the drawing is completed! 😱
- Win by revealing the word before your guesses run out.

---

## 📝 Example

```
Welcome to Hangman! 🕹️
_ _ _ _ _

Guess a letter: e
Correct! 🎉

_ e _ _ _

Guess a letter: a
Wrong! ❌ You have 5 attempts left.
```

---

## 🛠️ Customization

- Add more words to `words.txt` or the list in `hangman.py` 📚
- Change the ASCII art for a new hangman look 🎨
- Add hints, scoring, or even a GUI for extra fun!

---

## 🤝 Contributing

Contributions are welcome! Fork, clone, and submit a pull request 👍

---

## 📄 License

This project is licensed under the MIT License.

---

Enjoy playing Hangman! 🕵️‍♂️✨
