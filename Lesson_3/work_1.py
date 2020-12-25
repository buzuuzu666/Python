def my_func(a, b):
    try:
        return int(a / b)
    except (ZeroDivisionError):
        return "На 0 делить нельзя"


print(my_func(int(input("введите а = ")), int(input("введите b = "))))
