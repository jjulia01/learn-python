"""Задача 2024.10.16.01

Написать функцию для генерации строки из n строчных латинских букв"""

import random
def generate_random_string(n):
    random_letters='abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(random_letters)for _ in range(n))
if __name__=='__main__':
    n = 10
    result = generate_random_string(n)
    print(result)