from numpy import array

class Matrix:
    _array = None
    _column = None
    _line = None

    def __init__(self, _array):
        self._line = len(_array)
        self._column = len(_array[0])
        self._array = _array

    def __add__(self, other):
        array_new = [[0 for i in range(self._column)] for j in range(self._line)]
        for i in range(self._line):
            for j in range(self._column):
                array_new[i][j] = self._array[i][j] + other._array[i][j]
        return Matrix(array_new)

    def __sub__(self, other):
        array_new = [[0 for i in range(self._column)] for j in range(self._line)]
        for i in range(self._line):
            for j in range(self._column):
                array_new[i][j] = self._array[i][j] - other._array[i][j]
        return Matrix(array_new)

    def transposition(self):
        array_new = [[0 for i in range(self._line)] for j in range(self._column)]
        for i in range(self._line):
            for j in range(self._column):
                array_new[j][i] = self._array[i][j]
        return Matrix(array_new)

    def __eq__(self, other):
        if self is other:
            return True
        if self._column != other._column | self._line != other._line:
            return False
    
        for i in range(self._line):
            for j in range(self._column):
                if self._array[i][j] != other._array[i][j]:
                    return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f'Array \n'\
               f'{array(self._array)}\n'

if __name__ == '__main__':
    arr1 = Matrix([[10,4,5], [2,5,7], [1,2,3]])
    arr2 = Matrix([[10,4,5], [2,5,7], [1,2,3]])
    print(arr1)
    print(arr1 + arr2)
    print(arr1 - arr2)
    print(arr1.transposition())

    print(arr1 == arr2)
    print(arr1 != arr2)
