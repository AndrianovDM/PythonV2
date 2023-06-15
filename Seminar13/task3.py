class BaseException(Exception):
    pass

class LevelException(BaseException):
    def __init__(self, value, min_val):
        self.value = value
        self.min_val = min_val

    def __str__(self):
        return f'Ошибка уровня - {self.value}, минимальный необходимый уровень - {self.min_val}'
    
class AccessException(BaseException):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'Ошибка доступа - {self.value}'
