print("Установите имя")
name = input()

print("Установите PIN-код")
pin = int(input())

print("Установите баланс")
balance = int(input())

print("Здравствуйте, введите PIN-код")
entered_pin = int(input())

if entered_pin != pin:
    print("Неверный PIN! Карта заблокирована.")
    exit()

print(f"Добрый день, {name}!")
print(f"Ваш баланс: {balance}")
print("Выберите операцию: 1 - снять деньги, 2 - положить деньги, 3 - выйти")

operation = int(input())

if operation == 1:
    print("Введите сумму для снятия")
    amount = int(input())
    if amount > balance:
        print("Недостаточно средств")
    else:
        balance = balance - amount
        print(f"Успешно! Ваш новый баланс: {balance}")

elif operation == 2:
    print("Введите сумму пополнения")
    amount = int(input())
    balance = balance + amount
    print(f"Успешно! Ваш новый баланс: {balance}")

elif operation == 3:
    print("До свидания!")

else:
    print("Неизвестная операция!")