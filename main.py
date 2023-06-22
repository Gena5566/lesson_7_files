balance = 0
history = []

def add_money():
    global balance
    amount = float(input('Введите сумму для пополнения счета: '))
    balance += amount
    print(f'Баланс пополнен на {amount}. Текущий баланс: {balance}')

def buy_item():
    global balance, history
    amount = float(input('Введите сумму покупки: '))
    if amount > balance:
        print('На счету недостаточно денег!')
        return
    item = input('Введите название покупки: ')
    balance -= amount
    history.append((item, amount))
    print(f'Покупка "{item}" на сумму {amount} успешно проведена. Текущий баланс: {balance}')

def show_history():
    global history
    print('История покупок:')
    for item, amount in history:
        print(f'{item}: {amount}')

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
        break
    else:
        print('Неверный пункт меню')