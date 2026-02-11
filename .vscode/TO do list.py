import os

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            # strip() removes the extra newline \n
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

print("--- 2026 Task Manager ---")
todo_list = load_tasks()

while True:
    print("\n1. Show Tasks | 2. Add Task | 3. Remove Task | 4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nYOUR TASKS:")
        if not todo_list:
            print("The list is empty.")
        else:
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        new_task = input("What do you need to do? ")
        todo_list.append(new_task)
        save_tasks(todo_list)
        print("Task added!")

    elif choice == "3":
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            save_tasks(todo_list)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Not a valid choice, try again.") 