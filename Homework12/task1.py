import csv

class Assessment:
    def __init__(self, min: int=None, max: int=None):
        self.min = min
        self.max = max
    
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)
    
    def validate(self, value:int):
        if not isinstance(value, int):
            raise TypeError(f'Value {value} must be an integer')
        if self.min is not None and value < self.min:
            raise ValueError(f'Value {value} must be greater than or equal {self.min}')
        if self.max is not None and value > self.max:
            raise ValueError(f'Value {value} must be less {self.max}')

class Names:

    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value:str):
        if value.istitle() == False:
            raise ValueError(f'Value {value} must be capitalized ')
        if value.isalpha() == False:
            raise ValueError(f'Value {value} must not contain numbers')
        
class Subjects:
    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value:str):
        data = []
        with open('Subject.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                data.append(''.join(line)) 
                    
            if value not in data: 
                raise ValueError(f'Value {value} not on the list ')
        
class Student:
    last, first, father = Names(str), Names(str), Names(str)
    grade = Assessment(2, 5)
    exam = Assessment(0, 100)
    subject = Subjects(str)

    def __init__(self, last, first, father, subject, assessment, exam):
        self.last = last
        self.first = first
        self.father = father
        self.subject = subject
        self.exam = exam
        self.assessment = assessment


if __name__ == '__main__':
    student_1 = Student('Andrianov', 'Dmitry', 'Mikhailovich', 'Mathematics', 5, 100)
    student_2 = Student('Popov', 'Vitaly', 'Vladimirovich', 'Physics', 3, 60)