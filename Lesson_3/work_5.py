def my_func():
    result = 0
    while True:
        a = input("Введите число\n Для завершения программы нажмите q.").split()
        for num in a:
            if num == "q":
                return result
            else:
                try:
                    result += int(num)
                except ValueError:
                    print("Для выхода нажмите q")
        print(result)


print(my_func())
