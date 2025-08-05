# todo.py

def show_menu():
    print("\n🧠 Heron To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"✅ Task added: {task}")

def view_tasks():
    print("\n📋 Your Tasks:")
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No task file found yet.")

def complete_task():
    view_tasks()
    task_num = int(input("Enter the number of the task to mark as done: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print(f"❌ Removed task: {removed.strip()}")
    else:
        print("Invalid task number.")

# App loop
while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
