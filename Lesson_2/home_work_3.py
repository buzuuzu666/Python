n = int(float(input("Введите число от 1 до 12")))

if n <= 12 and n >= 1:
    my_dict = { 1: 'Jannuary',
                2: 'February',
                3: 'March',
                4: 'April',
                5: 'May',
                6: 'June',
                7: 'Jule',
                8: 'August',
                9: 'September',
                10: 'October',
                11: 'November',
                12: 'December'
    }
    my_list = list(my_dict.values())
    for i, el in enumerate((my_list),1):
        if i == n - 1:
            print(my_list[i])
else:
    print("Вы ввели не верное число")
