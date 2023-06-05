from random import randint

class Person:
    def __init__(self, last_name, first_name, second_name, birthday):
        self.__last_name = last_name
        self.__first_name = first_name 
        self.__second_name = second_name
        self.__birthday = birthday
    
    def get_birthday(self):
        return self.__birthday
    
    def add_birthday(self):
        self.__birthday += 1
    
    def get_fio(self):
        return f'{self.__last_name}, {self.__first_name}, {self.__second_name}'

class Employee(Person):

    def __init__(self, *args):
        super().__init__(*args)
        self.__id = randint(10 ** 5, 10 ** 6)
        self.__level = sum((int(i) for i in str(self.__id))) % 7
    
    def get_id(self):
        return self.__id

    def get_level(self):
        return self.__level
  
if __name__ == '__main__':
    person = Employee('Иванов', 'Иван', 'Иванович', 22)
    print(f'{person.get_fio() = }')
    print(f'{person.get_birthday() = }')
    person.add_birthday()
    print(f'{person.get_birthday() = }')   
    print(person.get_id(), person.get_level())