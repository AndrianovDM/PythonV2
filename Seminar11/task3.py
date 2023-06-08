class Archive:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.all_previous_numbers = list()
            cls._instance.all_previous_strings = list()

        else:
            cls._instance.all_previous_numbers.append(cls._instance.number)
            cls._instance.all_previous_strings.append(cls._instance.some_str)
        return cls._instance

    def __init__(self, number, some_str):
        self.number = number
        self.some_str = some_str

    def __str__(self):
        return f'Number: {self.number} ||| string: {self.some_str} |||'\
               f'archive: {list(zip(self.all_previous_numbers, self.all_previous_strings))}'


if __name__ == "__main__":
    arc1 = Archive(1, "str1")
    print(arc1)
    arc2 = Archive(2, "str2")
    print(arc2)
    arc3 = Archive(3, "str3")
    print(arc3)