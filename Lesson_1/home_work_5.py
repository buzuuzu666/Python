profit = int(input("Введите прибыль"))
damages = int(input("Введите убытки"))
if profit > damages:
    profitability = profit - damages
    print(f"У вас прибыльная фирма, прибыль составляет: {profitability} руб")
    employee = int(input("Введите число сотрудников"))
    employee = profitability / employee
    print(f"Прибыль на каждого сотрудника составляет {employee} руб")

else:
    print("Ваша фирма убыточная")
