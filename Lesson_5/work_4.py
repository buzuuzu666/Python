rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("work_44.txt", "w", encoding="utf-8") as pepe_1:
    with open("work_4.txt", encoding="utf-8") as pepe:
        pepe_1.writelines([line.replase(line.split()[0], rus.get(line.split()[0])) for line in pepe])
