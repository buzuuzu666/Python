a = str(input("Введите несколько слов через пробел"))
b = a.split()
for i, el in enumerate((b), 1):
    print(f"{i} {el[:10]}")
