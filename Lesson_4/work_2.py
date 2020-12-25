from random import randint

my_list = []
for _ in range(15):
    my_list.append(randint(1, 100))

print(my_list)

new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1]]

print(new_list)
