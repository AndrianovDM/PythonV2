# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

bank = 0
count = 0

def add_bank(cash: int) -> None:
    global bank, count
    bank += cash
    count += 1
    print('Ваш баланс: ', bank)

def take_bank(cash: int) -> None:
    global bank, count
    if cash <= 2000:
        cash -= 30
    elif 2001 <= cash <= 40000:
        cash *= 0.985
    else:
        cash -= 600
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
    print('Ваш баланс: ', bank)