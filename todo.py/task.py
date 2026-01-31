import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    try:
        selected_task_index = listbox.curselection()[0]
        task_text = listbox.get(selected_task_index)
        # Check if already marked
        if "✅" not in task_text:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, f"{task_text} ✅")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# 1. Create the main window
root = tk.Tk()
root.title("My Python To-Do List")
root.geometry("400x450")

# 2. Create the UI Elements
header_label = tk.Label(root, text="Task Manager", font=("Arial", 18, "bold"))
header_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4caf50", fg="white", width=20)
add_button.pack(pady=5)

# 3. The Listbox (where tasks appear)
listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
listbox.pack(pady=10, padx=20)

# 4. Action Buttons
done_button = tk.Button(root, text="Mark as Done", command=mark_done, bg="#2196f3", fg="white", width=20)
done_button.pack(pady=2)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#f44336", fg="white", width=20)
delete_button.pack(pady=2)

# 5. Start the Application
root.mainloop()