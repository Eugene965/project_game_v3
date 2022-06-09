"""Игра угадай число
Компьютер сам загадывает и сам угадывает число менее чем за 20 попыток
"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def search_limite(number) -> int:
    """Задаём пределы поиска загаданного числа

    Args:
        number: Загаданное число

    Returns:
        int: count, number: количество попыток и загаданное число
    """
    count = 0 # счетчик подходов
    
    # сужаем диапозон в котором находится загаданное число
    min = 1 # нижний предел
    max = 101 # верхний предел
    
    while True:
        count+=1
        mid = round((min+max) / 2) 
    
        if mid > number:
            max = mid
    
        elif mid < number:
            min = mid

        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break # конец игры выход из цикла

if __name__ == "__main__":
    search_limite(number)