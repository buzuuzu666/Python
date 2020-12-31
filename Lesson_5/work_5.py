from random import randint

with open("work_5.txt", "w", encoding="utf-8") as sum_numb:
    my_list = [randint(1, 100) for _ in range(10)]
    sum_numb.write(' '.join(map(str, my_list)))
print(f"Список чисел - {my_list}\nСумма чисел - {sum(my_list)}")
