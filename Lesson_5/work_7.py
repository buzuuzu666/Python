import json

with open("my.json", "w", encoding="utf-8") as ff:
    with open("work_7.txt", "r", encoding="utf-8") as firm:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in firm}
        res = [profit, {round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                              len([int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(res, ff, ensure_ascii=False, indent=4)


#Не знала как делается дз, списала с Вашего решения. Программа не работает почему-то.
