import time 

class Bankomat():
    def __init__(self, balance = 0.0):
        self.balance = balance
    
    def deposit_money(self):
        add_money = float(input("Введите сумму для депозита:"))
        self.balance += add_money
        print(f"Внесенная сумма:{add_money}")
        text_1 = open("deposit.txt", "a+")
        local_time = time.ctime()
        text_1.write(f"\nПополнения:{add_money}\n{local_time}")
        text_1.write(f"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    
    def withdraw_money(self):
        withdraw = float(input("Введите сумму вывода:"))
        print("Комиссия 1%")
        if self.balance >= withdraw * 1.01:
            self.balance -= withdraw * 1.01
            print(f"Вы сняли:{withdraw * 1.01}")
            local_time = time.ctime()
            text_2 = open("Cash.txt", "a+")
            text_2.write(f"\nВы сняли:{withdraw * 1.01}\n{local_time}")
            text_2.write(f"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        else:
            print("Не хватает денег!!!")
    
    def send_money(self):
        card = int(input("Введите номер карты получателя:"))
        send = float(input("Введите сумму отправки:"))
        print("Комиссия 1%")
        if self.balance >= send * 1.01:
            self.balance -= send * 1.01
            print(f"Вы отправили:{send * 1.01}")
            text_3 = open("Send.txt", "a+")
            local_time = time.ctime()
            text_3.write(f"\nБанковский аккаунт получателя: {card}")
            text_3.write(f"\nВы отправили:{send * 1.01}\n{local_time}")
            text_3.write(f"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        else:
            print("Не хватает денег!!!")



if __name__ ==  "__main__":
    bankomat = Bankomat()

    print("Добро пожаловать в банкомат Академии :)")
    print("Выберите операцию которую хотите выполнить: ")
    while 1:
        print("""                 1. Показать баланс
                 2. Внести деньги 
                 3. Снять деньги 
                 4. Отправить деньги
                 5. Завершить операцию""")
        x = int(input(":"))

        if x == 1:
            print(f"Текущий баланс = {bankomat.balance}")
        
        elif x == 2:
            bankomat.deposit_money()

        elif x == 3:
            bankomat.withdraw_money()
        
        elif x == 4:
            bankomat.send_money()
        elif x == 5:
            print(f"Спасибо что выбрали наш банк!!!")
