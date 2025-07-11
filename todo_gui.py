import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime, date

tasks = []

# Load and Save JSON
def load_tasks():
    global tasks
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

def save_tasks():
    tasks.sort(key=lambda t: t.get('due_date', '9999-12-31'))
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

# GUI functions
def refresh_list():
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    today = date.today()
    for idx, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        due = task.get('due_date', 'No Due Date')
        line = f"{idx}. {task['task']} [{status}] - Due: {due}\n"

        # Decide color
        color = "black"
        if task['done']:
            color = "green"
        else:
            if due != "No Due Date":
                try:
                    due_date = datetime.strptime(due, "%Y-%m-%d").date()
                    if due_date < today:
                        color = "red"
                except:
                    pass

        text_widget.insert(tk.END, line)
        text_widget.tag_add(f"line{idx}", f"{idx}.0", f"{idx}.end")
        text_widget.tag_config(f"line{idx}", foreground=color)

    text_widget.config(state=tk.DISABLED)

def add_task():
    task_text = simpledialog.askstring("New Task", "Enter task:")
    if not task_text:
        return
    due_date = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD) or leave blank:")
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format.")
            return
    else:
        due_date = "No Due Date"
    tasks.append({"task": task_text, "done": False, "due_date": due_date})
    save_tasks()
    refresh_list()

def mark_done():
    try:
        selection = int(simpledialog.askstring("Mark Done", "Enter task number to mark as done:"))
        if 1 <= selection <= len(tasks):
            tasks[selection - 1]['done'] = True
            save_tasks()
            refresh_list()
    except:
        pass

def delete_task():
    try:
        selection = int(simpledialog.askstring("Delete Task", "Enter task number to delete:"))
        if 1 <= selection <= len(tasks):
            del tasks[selection - 1]
            save_tasks()
            refresh_list()
    except:
        pass

def edit_task():
    try:
        selection = int(simpledialog.askstring("Edit Task", "Enter task number to edit:"))
        if 1 <= selection <= len(tasks):
            task = tasks[selection - 1]

            new_text = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=task['task'])
            if new_text:
                task['task'] = new_text

            new_due = simpledialog.askstring("Edit Due Date", "Edit due date (YYYY-MM-DD):", initialvalue=task.get('due_date', 'No Due Date'))
            if new_due:
                try:
                    datetime.strptime(new_due, "%Y-%m-%d")
                    task['due_date'] = new_due
                except ValueError:
                    messagebox.showerror("Invalid Date", "Invalid date format.")
            save_tasks()
            refresh_list()
    except:
        pass

# Setup window
root = tk.Tk()
root.title("To-Do List")

text_widget = tk.Text(root, width=70, height=20)
text_widget.pack(pady=10)
text_widget.config(state=tk.DISABLED)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Add Task", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Mark Done", command=mark_done).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Task", command=delete_task).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Edit Task", command=edit_task).grid(row=0, column=3, padx=5)

load_tasks()
refresh_list()

root.mainloop()
