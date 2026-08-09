def add_transaction(transactions, trans_type, category, amount, description):
    """Добавляет операцию в список"""
    transaction = {
        "type": trans_type,
        "category": category,
        "amount": amount,
        "description": description
    }
    transactions.append(transaction)
    print(f"Добавлено: {trans_type} — {category} — {amount} руб.")


def show_transactions(transactions):
    """Показывает все операции"""
    if len(transactions) == 0:
        print("Нет операций")
        return

    print("\nИстория операций:")
    print("-" * 50)
    for i, t in enumerate(transactions, start=1):
        sign = "+" if t["type"] == "доход" else "-"
        print(f"{i}. {sign}{t['amount']} руб. | {t['category']} | {t['description']}")
    print("-" * 50)


def get_balance(transactions):
    """Считает текущий баланс"""
    balance = 0
    for t in transactions:
        if t["type"] == "доход":
            balance += t["amount"]
        else:
            balance -= t["amount"]
    return balance


def get_stats_by_category(transactions):
    """Считает расходы по каждой категории"""
    stats = {}
    for t in transactions:
        if t["type"] == "расход":
            category = t["category"]
            if category in stats:
                stats[category] += t["amount"]
            else:
                stats[category] = t["amount"]
    return stats


def show_stats(transactions):
    """Показывает статистику по категориям"""
    stats = get_stats_by_category(transactions)

    if len(stats) == 0:
        print("Нет расходов для статистики")
        return

    print("\nРасходы по категориям:")
    print("-" * 30)

    sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)

    for category, amount in sorted_stats:
        print(f"  {category}: {amount} руб.")

    print("-" * 30)
    print(f"  Всего расходов: {sum(stats.values())} руб.")


def get_biggest_expense(transactions):
    """Находит самый большой расход"""
    expenses = [t for t in transactions if t["type"] == "расход"]

    if len(expenses) == 0:
        return None

    biggest = expenses[0]
    for t in expenses:
        if t["amount"] > biggest["amount"]:
            biggest = t

    return biggest


def show_menu():
    """Показывает меню"""
    print("\n=== Менеджер финансов ===")
    print("1. Добавить доход")
    print("2. Добавить расход")
    print("3. Показать баланс")
    print("4. Показать историю")
    print("5. Статистика по категориям")
    print("6. Самый большой расход")
    print("7. Выйти")


def main():
    transactions = []

    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            category = input("Категория (зарплата, фриланс, подарок): ")
            amount = float(input("Сумма: "))
            description = input("Описание: ")
            add_transaction(transactions, "доход", category, amount, description)

        elif choice == "2":
            category = input("Категория (еда, транспорт, жильё, развлечения): ")
            amount = float(input("Сумма: "))
            description = input("Описание: ")
            add_transaction(transactions, "расход", category, amount, description)

        elif choice == "3":
            balance = get_balance(transactions)
            print(f"\nБаланс: {balance} руб.")

        elif choice == "4":
            show_transactions(transactions)

        elif choice == "5":
            show_stats(transactions)

        elif choice == "6":
            biggest = get_biggest_expense(transactions)
            if biggest:
                print(f"\nСамый большой расход:")
                print(f"   {biggest['amount']} руб. — {biggest['category']} — {biggest['description']}")
            else:
                print("📭 Расходов нет")

        elif choice == "7":
            print("До свидания!")
            break

        else:
            print("Неизвестная команда!")


main()