class Generator:

    def __init__(self, *args):
        self.start, self.stop, self.step = 1, 1, 1
        match args:
            case (stop, ):
                self.stop = stop
            case (start, stop):
                self.start, self.stop = start, stop
            case (start, stop, step):
                self.start, self.stop, self.step = start, stop, step
            case _:
                raise AttributeError("Function takes up to 3 parameters: 'start', 'stop', 'step'")

        if self.start > self.stop:
            raise AttributeError("'start' parameter must be greater than or equal to 'stop' parameter")
        self.factorial = [*range(self.start, self.stop, self.step)]

    @staticmethod
    def calc(limit) -> int:
        if limit < 0:
            raise ValueError(f'Incompatible value (lesser than 0): {limit}')
        if limit in (0, 1):
            return 1
        else:
            result = 1
            for i in range(1, limit + 1):
                result *= i
            return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.factorial:
            return self.calc(self.factorial.pop(0))
        raise StopIteration

    def __str__(self):
        return f'Factorials range: {self.factorial}'


def main():
    factorials = Generator(6)
    # print(factorials)
    for i in factorials:
        print(i)
    # factorials = Generator(10, 10)
    # print(factorials)
    # for i in factorials:
    #     print(i)


if __name__ == '__main__':
    main()
