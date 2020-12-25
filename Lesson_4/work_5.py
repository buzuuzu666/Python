from functools import reduce

my_list = [el for el in range(1, 1001) if el % 2 == 0]


def res_list(a, b):
    return a * b

print(reduce(res_list, my_list))
