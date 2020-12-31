my_dict = {}
with open("work_6.txt", encoding="utf-8") as obj:
    for i in obj:
        thing, lesson = i.split(":")
        num_less = sum(map(int, "".join([a for a in lesson if a == " " or "9" >= a >= "0"]).split()))
        my_dict[thing] = num_less
print(my_dict)
