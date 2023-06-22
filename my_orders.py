import os

FILE_NAME = 'orders.txt'

balance = 0
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()
        if lines:
            last_line = lines[-1].strip()
            parts = last_line.split(': ')
            if len(parts) == 2:
                balance = float(parts[1].split(':')[0])




history = []

def save_balance():
    with open(FILE_NAME, "w") as f:
        f.write(f'Остаток на счету: {str(balance)}\n')
        f.write("История покупок:\n")
        for item in history:
            f.write(f'{str(item[0])}: {str(item[1])}\n')

def add_money():
    global balance
    amount = float(input('Введите сумму для пополнения счета: '))
    balance += amount
    history.append((balance, f'пополнение счета'))
    print(f'Баланс пополнен на {amount}. Текущий баланс: {balance}')
    save_balance()

def buy_item():
    global balance, history
    amount = float(input('Введите сумму покупки: '))
    if amount > balance:
        print('На счету недостаточно денег!')
        return
    item = input('Введите название покупки: ')
    balance -= amount
    history.append(f'{balance}: покупка - "{item}"')  # Сохранить в формате "баланс: покупка - "item""
    print(f'Покупка "{item}" на сумму {amount} успешно проведена. Текущий баланс: {balance}')
    save_balance()


def show_history():
    print('История покупок:')
    for item in history:
        print(item)

# Основной код программы
while True:
    print('1. Пополнение счета')
    print('2. Покупка')
    print('3. История покупок')
    print('4. Выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        add_money()
    elif choice == '2':
        buy_item()
    elif choice == '3':
        show_history()
    elif choice == '4':
        save_balance()
        break
    else:
        print('Неверный пункт меню')



