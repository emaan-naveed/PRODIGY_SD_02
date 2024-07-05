import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")
        master.configure(bg='red')

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="I have selected a number between 1 and 100. Can you guess it?", bg='red', fg='white', font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.entry = tk.Entry(master, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, bg='white', fg='red', font=("Helvetica", 14))
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", bg='red', fg='white', font=("Helvetica", 14))
        self.result_label.pack(pady=20)

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.number_to_guess:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.number_to_guess:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text=f"Congratulations! You've guessed the number {self.number_to_guess} correctly in {self.attempts} attempts.")
            self.guess_button.config(state=tk.DISABLED)
            self.entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
