def my_func(a_1, a_2, a_3):
    a = [a_1, a_2, a_3]
    b = []
    b.append(max(a))
    a.remove(max(a))
    b.append(max(a))
    print(sum(b))


my_func(120, 4, 50)