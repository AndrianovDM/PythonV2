# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.


def main() :
    solve([])

COLUMNS = "abcdefgh"
NQUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3

def attacks(p1, p2) :
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])
    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])
    return (row1 == row2 or column1 == column2 or abs(row1 - row2) == abs(column1 - column2))

def extend(partialSolution) :
    results = []
    row = len(partialSolution) + 1
    for column in COLUMNS :
        newSolution = list(partialSolution)
        newSolution.append(column + str(row))
        results.append(newSolution)
    return results

def examine(partialSolution) :
    for i in range(0, len(partialSolution)) :
        for j in range(i + 1, len(partialSolution)) :
            if attacks(partialSolution[i], partialSolution[j]) :
                return ABANDON
    if len(partialSolution) == NQUEENS :
        return ACCEPT
    else :
        return CONTINUE
    
def solve(partialSolution) :
    exam = examine(partialSolution)
    if exam == ACCEPT :
        print(partialSolution)
    elif exam != ABANDON :
        for p in extend(partialSolution) :
            solve(p)

main()

