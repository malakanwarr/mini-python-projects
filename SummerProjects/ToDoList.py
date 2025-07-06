tasks = []
while True:
    print("Welcome to your To-Do List!")
    print("What do you want to do?")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("You have no tasks.")
        else:
            print("Your Tasks:")
            i = 1
            for task in tasks:
                print(f"{i}. {task}")
                i += 1
    elif choice == "3":
        if not tasks:
            print("You have no tasks to remove.")
        else:
            print("Which task number do you want to remove?")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter number: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose from 1 to 4.")
