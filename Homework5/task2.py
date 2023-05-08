# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии 

def stake(name: list[str], cash: list[int], percent: list[str]) -> dict[str:float]:
    return {name: money / 100 * perc for name, money, perc in zip(name, cash, (float(i[:-1]) for i in percent))}

print(stake(name = ['stake1', 'stake2', 'stake3'], cash = [100, 150, 265], percent =['10.25%', '12.25%', '15.25%']))