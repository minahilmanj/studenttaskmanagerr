
tasks = []
next_id = 1



def add_task():
    global next_id

    title = input("Enter task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
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


def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
