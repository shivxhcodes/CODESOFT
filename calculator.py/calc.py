import tkinter as tk
from tkinter import messagebox

# --- Logic Function ---
def calculate(operation):
    try:
        # 1. Get the numbers from the entry boxes
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # 2. Perform the math based on the button clicked
        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
            
        # 3. Update the result label
        label_result.config(text=f"Answer: {result}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# --- Window Setup ---
root = tk.Tk()
root.title("Simple Calc")
root.geometry("300x350")

# --- UI Elements ---
tk.Label(root, text="Enter First Number:", pady=5).pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number:", pady=5).pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Operations:", pady=10).pack()

# --- Buttons ---
# We use 'lambda' to pass a specific word to our function
btn_frame = tk.Frame(root) # A frame helps us group buttons together
btn_frame.pack()

tk.Button(btn_frame, text="+", width=5, command=lambda: calculate("add")).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="-", width=5, command=lambda: calculate("sub")).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="*", width=5, command=lambda: calculate("mul")).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="/", width=5, command=lambda: calculate("div")).grid(row=1, column=1, padx=5, pady=5)

# --- Result ---
label_result = tk.Label(root, text="Answer: ", font=("Arial", 14, "bold"), pady=20)
label_result.pack()

root.mainloop()