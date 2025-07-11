import json
import os
from datetime import datetime,date

tasks = []

def load_tasks():
    global tasks
    file_path = os.path.join(os.getcwd(), "tasks.json")
    print(f"[DEBUG] Looking for tasks.json at: {file_path}")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            tasks = json.load(f)
        print("[DEBUG] tasks.json found and loaded.")
        sort_tasks()
    else:
        tasks = []
        print("[DEBUG] tasks.json does not exist yet.")


def save_tasks():
    sort_tasks() 
    file_path = os.path.join(os.getcwd(), "tasks.json")
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=4)
    print(f"[DEBUG] tasks.json saved at: {file_path}")


def sort_tasks():
    def get_due_date(task):
        due_date = task.get("due_date", "No Due Date")
        if due_date == "No Due Date":
            return datetime.max
        try:
            return datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            return datetime.max
    tasks.sort(key=get_due_date)


def show_menu():
    print("\n======= TO-DO LIST MENU =======")
    print("1.View Task")
    print("2.Add Task")
    print("3.Mark Task as Complected")
    print("4.Delet The Task")
    print("5.Edit Task")
    print("6.Exit")

def view_tasks():
    today = date.today()   
    sort_tasks()
    if not tasks:
        print("\nYour to-do list is empty")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['done'] else "Not Done"
            due_date = task.get('due_date', 'No Due Date')
            overdue = ""
            if due_date and due_date != 'No Due Date':
                try:
                    due = datetime.strptime(due_date, "%Y-%m-%d").date()
                    if not task['done'] and due < today:
                        overdue = " (OVERDUE!)"
                except ValueError:
                    overdue = " (Invalid date)"
            print(f"{i}. {task['task']}  [{status}] - Due: {due_date}{overdue}")



def add_task():
    task_name = input("Enter the task:").strip()
    if not task_name:
        print("Task cannot be empty:")
        return
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Task not added.")
            return
    else:
        due_date = "No Due Date"
    tasks.append({"task": task_name, "done": False, "due_date": due_date})
    save_tasks()
    print(f"Task '{task_name}' added with due date: {due_date}")
    view_tasks()


def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to mark as completed:"))
        if 1 <= task_no <= len(tasks):
            tasks[task_no - 1]['done'] = True
            save_tasks()
            print(f"Task {task_no} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delet_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to delect:"))
        if 1 <= task_no <= len(tasks):
            remove = tasks.pop(task_no - 1)
            save_tasks()
            print(f"Task '{remove['task']}' delected.") 
        else:
            print("Invalid task  number.") 
    except ValueError:
        print("Please enter a valid number.") 


def edit_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_no = int(input("Enter task number to edit: "))
        if 1 <= task_no <= len(tasks):
            task = tasks[task_no - 1]
            new_text = input(f"Enter new task text (leave blank to keep '{task['task']}'): ").strip()
            if new_text:
                task['task'] = new_text

            current_due_date = task.get('due_date', 'No Due Date')
            new_due_date = input(f"Enter new due date (YYYY-MM-DD) or leave blank to keep '{current_due_date}': ").strip()
            if new_due_date:
                try:
                    datetime.strptime(new_due_date, "%Y-%m-%d")
                    task['due_date'] = new_due_date
                except ValueError:
                    print("Invalid date format. Due date not changed.")
            elif 'due_date' not in task:
                # If there was no due_date and user didn't provide one
                task['due_date'] = "No Due Date"

            save_tasks()
            print(f"Task {task_no} updated.")
            view_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


load_tasks()


while True:
    show_menu()
    choice = input("Enter your choice(1-5): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delet_task()
    elif choice == '5':
        edit_task()    
    elif choice == '6':
        print("Goodbye")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5")