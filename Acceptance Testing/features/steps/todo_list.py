class Task:
    def __init__(self, description, status="Pending"):
        self.description = description
        self.status = status


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for task in self.tasks:
            print(task.description)

    def mark_task_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.status = "Completed"

    def mark_task_pending(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.status = "Pending"

    def clear_tasks(self):
        self.tasks = []


"""
if __name__ == "__main__":
    todo_manager = ToDoListManager()

    def display_menu():
        print("\nMenu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Mark Task as Pending")
        print("5. Clear All Tasks")
        print("6. Exit")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_manager.add_task(description)
            print("Task added!")

        elif choice == "2":
            print("\nTasks:")
            todo_manager.list_tasks()

        elif choice == "3":
            description = input("Enter task description to mark as completed: ")
            task = todo_manager.find_task(description)
            if task:
                todo_manager.mark_task_completed(description)
                print("Task marked as completed!")
            else:
                print("Task not found.")

        elif choice == "4":
            description = input("Enter task description to mark as pending: ")
            task = todo_manager.find_task(description)
            if task:
                todo_manager.mark_task_pending(description)
                print("Task marked as pending!")
            else:
                print("Task not found.")

        elif choice == "5":
            todo_manager.clear_tasks()
            print("All tasks cleared!")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")
"""
