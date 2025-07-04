# To-Do List Application

# Shows the main menu to the user
def display_menu():
    """Display the main menu options."""
    print("\n=== TO-DO LIST APPLICATION ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

# Adds a new task to the task list
def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task you want to add: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("Task cannot be empty.")

# Shows all current tasks to the user
def view_tasks(tasks):
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


# Deletes a task based on the number the user enters
def delete_task(tasks):
    """Delete a task by its number in the list."""
    if not tasks:
        print("There are no tasks to delete.")
        return
    
    view_tasks(tasks)

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Runs the main loop of the app and handles user input
def main():
    """Main function to run the To-Do List application."""
    tasks = []
    while True:
        display_menu()
        try:
            choice = input("Select an option (1-4): ").strip()
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                delete_task(tasks)
            elif choice == '4':
                print("Thank you for using the To-Do List Application. Goodbye!")
                break
            else:
                print("Invalid selection. Please choose a number between 1 and 4.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("\nReturning to main menu...")

# Starts the application when the script is run
if __name__ == "__main__":
    main()
