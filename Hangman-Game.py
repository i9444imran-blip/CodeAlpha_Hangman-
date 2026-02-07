import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("700x700")
        self.root.configure(bg='lightblue')
        
        
        self.words = ['PYTHON', 'JAVA', 'APPLE', 'MOUSE', 'WINDOW', 
                     'GOOGLE', 'FACEBOOK', 'TWITTER', 'LAPTOP', 'MOBILE']
        
        
        self.clues = {
            'PYTHON': 'A programming language',
            'JAVA': 'Another programming language',
            'APPLE': 'A fruit and a company',
            'MOUSE': 'Computer device',
            'WINDOW': 'Part of a house',
            'GOOGLE': 'Search engine',
            'FACEBOOK': 'Social media',
            'TWITTER': 'Social media with birds',
            'LAPTOP': 'Portable computer',
            'MOBILE': 'Smartphone'
        }
        
        
        self.word = ""
        self.clue = ""
        self.guessed_word = []
        self.wrong_guesses = 0
        self.max_wrong = 6
        self.guessed_letters = []
        self.score = 0
        
        self.setup_gui()
        self.start_game()
    
    def setup_gui(self):
       
        title_label = tk.Label(
            self.root,
            text="HANGMAN GAME",
            font=('Arial', 30, 'bold'),
            bg='lightblue',
            fg='darkblue'
        )
        title_label.pack(pady=10)
        
        
        self.score_label = tk.Label(
            self.root,
            text=f"Score: {self.score}",
            font=('Arial', 14),
            bg='lightblue',
            fg='green'
        )
        self.score_label.pack()
        
       
        self.canvas = tk.Canvas(
            self.root,
            width=300,
            height=250,
            bg='white'
        )
        self.canvas.pack(pady=10)
        
        
        self.word_label = tk.Label(
            self.root,
            text="",
            font=('Courier', 24),
            bg='lightblue',
            fg='black'
        )
        self.word_label.pack(pady=10)
        
       
        self.clue_label = tk.Label(
            self.root,
            text="",
            font=('Arial', 12, 'italic'),
            bg='lightblue',
            fg='purple'
        )
        self.clue_label.pack()
        
       
        self.wrong_label = tk.Label(
            self.root,
            text="",
            font=('Arial', 12),
            bg='lightblue',
            fg='red'
        )
        self.wrong_label.pack()
        
        
        letters_frame = tk.Frame(self.root, bg='lightblue')
        letters_frame.pack(pady=20)
        

        self.letter_buttons = {}
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        row1_frame = tk.Frame(letters_frame, bg='lightblue')
        row1_frame.pack()
        
        for i in range(13):
            letter = letters[i]
            btn = tk.Button(
                row1_frame,
                text=letter,
                width=4,
                height=2,
                font=('Arial', 10, 'bold'),
                command=lambda l=letter: self.guess(l),
                bg='lightgray',
                activebackground='yellow'
            )
            btn.pack(side='left', padx=2, pady=2)
            self.letter_buttons[letter] = btn
        
        row2_frame = tk.Frame(letters_frame, bg='lightblue')
        row2_frame.pack()
        
        for i in range(13, 26):
            letter = letters[i]
            btn = tk.Button(
                row2_frame,
                text=letter,
                width=4,
                height=2,
                font=('Arial', 10, 'bold'),
                command=lambda l=letter: self.guess(l),
                bg='lightgray',
                activebackground='yellow'
            )
            btn.pack(side='left', padx=2, pady=2)
            self.letter_buttons[letter] = btn
        
        control_frame = tk.Frame(self.root, bg='lightblue')
        control_frame.pack(pady=10)
        
        tk.Button(
            control_frame,
            text="New Game",
            font=('Arial', 12, 'bold'),
            command=self.start_game,
            bg='green',
            fg='white',
            width=12,
            height=2
        ).pack(side='left', padx=10)
        
        tk.Button(
            control_frame,
            text="Get Hint",
            font=('Arial', 12, 'bold'),
            command=self.get_hint,
            bg='orange',
            fg='white',
            width=12,
            height=2
        ).pack(side='left', padx=10)
        
        self.status_label = tk.Label(
            self.root,
            text="Game started! Guess a letter!",
            font=('Arial', 12),
            bg='lightblue',
            fg='blue'
        )
        self.status_label.pack(pady=10)
    
    def start_game(self):
        self.word = random.choice(self.words)
        self.clue = self.clues[self.word]
        self.guessed_word = ['_'] * len(self.word)
        self.wrong_guesses = 0
        self.guessed_letters = []
        
        
        self.update_display()
        
        for btn in self.letter_buttons.values():
            btn.config(state='normal', bg='lightgray')
        
        self.canvas.delete("all")
        
        self.status_label.config(text="New game started! Guess a letter!")
    
    def update_display(self):
        display_word = ' '.join(self.guessed_word)
        self.word_label.config(text=display_word)
        
        self.clue_label.config(text=f"Clue: {self.clue}")
        
        self.wrong_label.config(text=f"Wrong guesses: {self.wrong_guesses}/{self.max_wrong}")
        
        self.score_label.config(text=f"Score: {self.score}")
        
        self.draw_hangman()
        
        self.check_game()
    
    def draw_hangman(self):
        self.canvas.delete("all")
        
        
        self.canvas.create_line(50, 200, 150, 200, width=4)
        self.canvas.create_line(100, 200, 100, 50, width=4)
        self.canvas.create_line(100, 50, 150, 50, width=4)
        self.canvas.create_line(150, 50, 150, 70, width=2)
        
        if self.wrong_guesses >= 1:
            self.canvas.create_oval(140, 70, 160, 90, width=3)
        

        if self.wrong_guesses >= 2:
            self.canvas.create_line(150, 90, 150, 140, width=3)
        
        if self.wrong_guesses >= 3:
            self.canvas.create_line(150, 100, 130, 120, width=3)
        
        if self.wrong_guesses >= 4:
            self.canvas.create_line(150, 100, 170, 120, width=3)
        
        if self.wrong_guesses >= 5:
            self.canvas.create_line(150, 140, 130, 170, width=3)
        
        if self.wrong_guesses >= 6:
            self.canvas.create_line(150, 140, 170, 170, width=3)
    
    def guess(self, letter):
        if letter in self.guessed_letters:
            self.status_label.config(text=f"Already guessed {letter}!")
            return
        
        self.guessed_letters.append(letter)
        self.letter_buttons[letter].config(state='disabled')
        
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guessed_word[i] = letter
            self.letter_buttons[letter].config(bg='lightgreen')
            self.score += 10
            self.status_label.config(text=f"Good! {letter} is correct!")
        else:
            self.wrong_guesses += 1
            self.letter_buttons[letter].config(bg='red')
            self.score = max(0, self.score - 5)
            self.status_label.config(text=f"Wrong! {letter} is not in the word!")
        
        self.update_display()
    
    def get_hint(self):
       
        hidden = []
        for i in range(len(self.guessed_word)):
            if self.guessed_word[i] == '_':
                hidden.append(i)
        
        if not hidden:
            self.status_label.config(text="No more hints needed!")
            return
        
        
        pos = random.choice(hidden)
        letter = self.word[pos]
        
        if letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            self.letter_buttons[letter].config(state='disabled', bg='yellow')
        
       
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.guessed_word[i] = letter
        
        self.score = max(0, self.score - 20)
        self.status_label.config(text=f"Hint: Letter {letter} revealed!")
        self.update_display()
    
    def check_game(self):
        if '_' not in self.guessed_word:
            self.score += 100
            for btn in self.letter_buttons.values():
                btn.config(state='disabled')
            self.status_label.config(text=f"You win! The word was {self.word}")
            messagebox.showinfo("You Win!", f"Congratulations!\nThe word was: {self.word}\nScore: {self.score}")
        
       
        elif self.wrong_guesses >= self.max_wrong:
            for btn in self.letter_buttons.values():
                btn.config(state='disabled')
           
            self.guessed_word = list(self.word)
            self.update_display()
            self.status_label.config(text=f"Game over! The word was {self.word}")
            messagebox.showinfo("Game Over", f"Game Over!\nThe word was: {self.word}")

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()