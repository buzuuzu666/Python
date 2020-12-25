number = int(input("Введите время в секундах"))

s = number % 60
number = number - s
h = number // 3600
number = number - (h * 3600)
m = number // 60

print(f"{h:02d}:{m:02d}:{s:02d}")
