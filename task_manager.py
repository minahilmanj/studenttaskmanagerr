
tasks = []
next_id = 1


# Function to add a new task
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


# Function to display all tasks
def display_tasks():
    print("\n--- Student Task Manager ---")

    if not tasks:
        print("No tasks available.")
        return

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


# Function to mark a task as completed
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
            if task["completed"]:
                print("This task is already completed.")
            else:
                task["completed"] = True
                print("Task marked as completed!")
            return

    print("Task ID not found.")


# Function to delete a task
def delete_task():
    display_tasks()

    if not tasks:
        return

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")
            return

    print("Task ID not found.")


# Main menu function
def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            display_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


# Program execution starts here
if __name__ == "__main__":
    main()
