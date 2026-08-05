tasks = []

while True:
    print("\n=== Менеджер задач ===")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append(task)
        print(f"Задача '{task}' добавлена!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Список пуст!")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Нечего удалять!")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

            number = int(input("Введите номер задачи для удаления: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"Задача '{removed}' удалена!")
            else:
                print("Неверный номер задачи!")

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Неизвестная команда!")