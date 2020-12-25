from sys import argv

name, clock, rate, prize = argv
try:
    res = (int(clock) * int(rate)) + int(prize)
    print(res)
except ValueError:
    print("Вводить нужно только целые числа")
