a = int(input("Введите результат бега в км"))
b = int(input("Введите сколько км нужно пробежать "))
c = 10
day = 1
c = c / 100

while a <= b:
    a = a + (a * c)
    day += 1

if a > b:
    print(f"Вы прообежите не менее {b} км на {day} день пробежки")
