with open("text_303.txt", "w", encoding="utf-8") as heroe:
    while True:
        a = str(input("Введите данные для записи в файл, для выхода нажать Enter"))
        if a == "":
            break
        else:
            content_2 = heroe.write(f"{a}\n")
"""Вывод информации"""
with open("text_303.txt", "r", encoding="utf-8") as heroes:
    content_3 = heroes.read()
    print(content_3)
