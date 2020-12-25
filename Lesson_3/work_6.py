"""Первый вариант решения c 1 словом"""


def my_func(r):
    return r.title()


print(my_func(input("Введите слово")))

"""Второй вариант решения с предложением"""

a = input("введите предложение").split()
for i in a:
    result = my_func(i)  # обращаемся к уже существующей фенкции
    if result:
        print(my_func(i))
