# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.
import os

def info(path_file):
    path, file_name = os.path.split(path_file)
    name, extension = os.path.splitext(file_name)
    return path, name, extension

print(info('B:\Postgraduate studies\Homework program'))