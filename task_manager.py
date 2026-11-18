
tasks = []
next_id = 1


def add_task():
    global next_id

    title = input("Enter task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
        return

    if len(title) > 100:
        print("Error: Task title cannot exceed 100 characters.")
        return

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    next_id += 1

    print("Task added successfully!")


def display_tasks():
    print("\n--- Student Task Manager ---")

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


def complete_task():
    display_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to complete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print("Task marked as completed!")
            return

    print("Task ID not found.")


def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
