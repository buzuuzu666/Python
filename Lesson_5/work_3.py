employee = []
count = 0
sam = 0
with open("work_3.txt", "r", encoding="utf-8") as income:
    try:
        for i in income:
            print(i, end="")
            divider = i.split(":")
            if int(divider[1]) <= 20000:
                employee.append(divider[0])
                sam += int(divider[1])
                count += 1
            else:
                sam += int(divider[1])
                count += 1
        res = sam / count
        a = ", ".join(employee).split()
        print(f"\nМеньше 20к зарабатывают:", *a, "\n" f"Средний доход всех сотрудников: {res:.2f}")
    except ValueError:
        print("\n", f"Что-то пошло не так. После числа есть буквы")
