# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

bank = 0
count = 0
list_operations = []

def add_bank(cash: int) -> None:
    global bank, count, list_operations
    bank += cash
    list_operations.append(f'+{cash}')
    count += 1
    print('Ваш баланс: ', bank)

def take_bank(cash: int) -> None:
    global bank, count, list_operations
    if cash <= 2000:
        cash -= 30
        list_operations.append(f'{cash}')
    elif 2001 <= cash <= 40000:
        cash *= 0.985
        list_operations.append(f'{cash}')
    else:
        cash -= 600
        list_operations.append(f'{cash}')
    bank -=cash
    count += 1
    print('Ваш баланс: ', bank)

def exit_bank():
    print('Рады видеть вас снова!')
    exit()

def check_bank() -> int:
    while True:
        cash = int(input('Введите функцию, кратную 50'))
        if cash % 50 == 0:
            return cash


while True:
    action = input('1 - снять\n2 - пополнить\n3 - выйти\n')
    if bank >= 5_000_000:
        bank *= 0.9
    match action:
        case '1':
            if cash := check_bank() < bank:
                take_bank(cash)
            else:
                print('Нет денег!')
        case '2':
            add_bank(check_bank())
        case '3':
            exit_bank()
    if count == 3:
        bank *= 1.03
        count = 0
    print('Операции по счету:', list_operations)
