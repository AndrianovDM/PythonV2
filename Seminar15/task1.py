# 
import logging

logging.basicConfig(
    filename = 'Task1.log',
    filemode = 'w',
    encoding = 'utf8',
    format = '{asctime} {levelname:<8} функций "{funcName}()" строка {lineno:>3d} : {msg}',
    style = '{',
    level = logging.ERROR)
logger = logging.getLogger(__name__)

def div(a, b):
    try:
        res = a/b
    except:
        logger.error(f'Ошибка деления на ноль! Число {a} делится на {b}!')
        return float('inf')
    return res

if __name__ == '__main__':
    print(div(2,0))