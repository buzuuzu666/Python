from itertools import count
from math import factorial

"""Функция возвращает факториал"""
def my_gen():
    for i in count(1):
        yield factorial(i)


a = 0
for el in my_gen():
    if a < 5:  #назначаем факториал какого числа искать (5)
        print(el)
        a += 1
    else:
        break
