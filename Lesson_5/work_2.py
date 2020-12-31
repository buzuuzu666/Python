with open("work_2.txt", "r", encoding="utf-8") as forest:
    a = [f"{line}) {' '.join(count.split())} - {len(count.split())} слов" for line, count in enumerate(forest, 1)]
    print(a, f"кол-вo строк - {len(a)}", sep='\n')
