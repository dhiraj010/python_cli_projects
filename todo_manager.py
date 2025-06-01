tasks = [
            {"task": "Study Python", "status": "Pending"},
            {"task": "Buy Milk", "status": "Done"}
        ]


# tasks = []
def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks):
             print(f"{i +1}. {task['task']} - {task['status']}")

def add_task():
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "status": "Pending"})
    print("Task added!")


def mark_done():
    show_tasks()
    task_no = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no]["status"] = "Done"
        print("Task marked as done!")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    task_no = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_no < len(tasks):
        deleted = tasks.pop(task_no)
        print(f"Deleted: {deleted['task']}")
    else:
        print("Invalid task number.")

def menu():
    print("\n===== TO-DO MANAGER =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")



while True:
    menu()
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")