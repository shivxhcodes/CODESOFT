import tkinter as tk
import random
from tkinter import messagebox

# Initialize scores
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    
    # 1. Computer makes a random choice
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)
    
    # 2. Determine the winner
    result = ""
    if user_choice == comp_choice:
        result = "It's a Tie! 🤝"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "Computer Wins! 🤖"
        comp_score += 1
    
    # 3. Update the UI labels
    label_choices.config(text=f"You: {user_choice}  |  PC: {comp_choice}")
    label_result.config(text=result)
    label_score.config(text=f"Score - You: {user_score}  Computer: {comp_score}")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    label_choices.config(text="Make your move!")
    label_result.config(text="Waiting...")
    label_score.config(text="Score - You: 0  Computer: 0")

# --- GUI Setup ---
root = tk.Tk()
root.title("Rock Paper Scissors Pro")
root.geometry("400x450")
root.config(bg="#f0f0f0")

# Header
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

# Scoreboard
label_score = tk.Label(root, text="Score - You: 0  Computer: 0", font=("Arial", 12), bg="#f0f0f0")
label_score.pack()

# Choice/Result Display
label_choices = tk.Label(root, text="Make your move!", font=("Arial", 12, "italic"), pady=10, bg="#f0f0f0")
label_choices.pack()

label_result = tk.Label(root, text="Waiting...", font=("Arial", 16, "bold"), fg="#2196f3", bg="#f0f0f0")
label_result.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=20)

# Use lambda to pass the choice to the function
tk.Button(btn_frame, text="🪨 Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="📜 Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="✂️ Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Reset Button
tk.Button(root, text="Reset Scores", command=reset_game, bg="#9e9e9e", fg="white").pack(pady=20)

root.mainloop()