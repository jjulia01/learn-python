"""Задача 2024.10.16.02

Написать функцию для генерации строки из n строчных и заглавных латинских букв
Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
А если параметр use_uppercase не указан при использовании функции, то генерируем строку только из строчных букв."""

import random
from string import ascii_lowercase, ascii_uppercase

def generate_random_string(n:int, uppercase:bool=False)->str:
    char:str=ascii_lowercase
    if uppercase:char+=ascii_uppercase
    return ''.join(random.choice(char)for _ in range(n))
if __name__=='__main__':
    print(generate_random_string(20,True))
