# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import datetime

class MyStr(str):
    def __new__(cls, value, author_name):
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.creation_time = datetime.datetime.now()
        return instance
    
if __name__ == "__main__":
    s = MyStr("stroka", "Dima")
    print(s, s.author_name, s.creation_time)
    print(s.upper())