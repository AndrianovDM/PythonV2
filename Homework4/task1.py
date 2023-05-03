# Напишите функцию для транспонирования матрицы

matrix = [[1,2],[3,4],[5,6]]

def transpositions(data: list[int | float]) -> None:
    trans_matrix = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    return trans_matrix

print('Исходная матрица: ', matrix)
print('Транспонированная матрица: ', transpositions(matrix))

