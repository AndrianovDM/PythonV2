# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только 
# на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

flag = False
while flag != True:
    number = int(input("Введите число:"))
    if 0 < number < 10e4:
        k = 0
        for i in range(2, number // 2+1):
            if (number % i == 0):
                k = k+1
        if k <= 0:
            print("Число целочисленное")
            flag = True
        else:
            print("Число составное")
            flag = True
    else:
        flag = False




