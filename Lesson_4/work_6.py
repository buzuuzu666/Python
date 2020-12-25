from itertools import count, cycle

whole_num = []
for i in count(3):
    if i <= 10:
        whole_num.append(i)
    else:
        break

print(whole_num)

my_list = []
for el in cycle([1, "two", 3]):
    if len(my_list) <= 9:
        my_list.append(el)
    else:
        break

print(my_list)
