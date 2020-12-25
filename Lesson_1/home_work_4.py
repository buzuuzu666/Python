n = int(input("Введите целое число"))

while n < 0:
    n = int(input("Введите положительное число"))

top = -1

while n > 10:
    d = n % 10
    n //= 10
    if d > top:
        top = d
print(top)
