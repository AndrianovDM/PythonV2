import argparse
import logging

form = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level = logging.INFO,
                    filename = 'Task1.log', 
                    encoding = 'utf-8',
                    format = form, 
                    style = '{')
logger = logging.getLogger(__name__)

def convert(num, base):
    result = ''
    if base < 0:
        logger.error(f'Такой системы исчисления {base} нет')
        return float('inf')
    
    while num != 0:
        try:
            result = str(num % base) + result
            num //= base

        except ZeroDivisionError as e:
            logger.error(f'Такой системы исчисления {base} нет')
            return float('inf')
        
    logger.info(f'{num}, {base} = {result}')
    return result

def pars():
    pars = argparse.ArgumentParser(description ='Получаем аргументы')
    pars.add_argument('--num')
    pars.add_argument('--base', default=10)
    args = pars.parse_args()
    print(args)
    return convert(int(args.num), int(args.base))

if __name__ == '__main__':
    print(convert(123, 1))
    print(convert(123, 0))
    print(convert(123, -20))
    pars()