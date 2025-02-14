import os

FILENAME = "todos.txt"


def load_tasks():
    tasks = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            tasks = file.read().splitlines()
    return tasks


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("=" * 30)
        print("✅ Your TODO list is empty!")
        print("=" * 30)
    else:
        print("\n📝 Your TODO list:")
        print("=" * 30)
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print("=" * 30)


def add_task(tasks):
    task = input("\n➕ Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("=" * 30)
        print("✅ Task added!")
        print("=" * 30)


def remove_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("\n❌ Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            save_tasks(tasks)
            print("=" * 30)
            print("✅ Task removed!")
            print("=" * 30)
        else:
            print("=" * 30)
            print("❌ Invalid task number")
            print("=" * 30)
    except ValueError:
        print("=" * 30)
        print("❌ Please enter a valid number!")
        print("=" * 30)


def main():
    tasks = load_tasks()

    while True:
        print("#" * 30)
        print("\t📌 TODO APP")
        print("#" * 30)
        print("\t1️⃣ View Tasks")
        print("\t2️⃣ Add Task")
        print("\t3️⃣ Remove Task")
        print("\t4️⃣ Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("\nYour tasks are saved.")
            break
        else:
            print("❌ Invalid choice! Please enter 1-4.")


if __name__ == "__main__":
    main()
