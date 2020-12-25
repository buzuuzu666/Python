my_list = [7, 5, 3, 3, 2]

while True:
    a = int(float(input("Введите число")))
    b = my_list.count(a)
    for i in my_list:
        if b > 0:
            c = my_list.index(a)
            my_list.insert(c + b, a)
            print(my_list)
            break
        else:
            if a > i:
                d = my_list.index(i)
                my_list.insert(d, a)
                print(my_list)
                break
            elif a < my_list[len(my_list) - 1]:
                my_list.append(a)
                print(my_list)


