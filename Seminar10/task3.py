class Animal:
    def __init__(self, name, age, ):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
class Fish(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color

    def get_specific(self):
        return self.__color

class Mammal(Animal):
    def __init__(self, name, age, wool):
        super().__init__(name, age)
        self.__wool = wool

    def get_specific(self):
        return self.__wool

class Bird(Animal):
    def __init__(self, name, age, feather):
        super().__init__(name, age)
        self.__feather = feather

    def get_specific(self):
        return self.__feather
