"""Задание 3 — read(), readline(), cursor
Создай файл:
one
two
three
four
Открой его один раз и последовательно сделай:
f.readline()
f.readline()
f.tell()
f.readline()
Посмотри результаты.
После этого:
f.seek(0)
и снова:
f.readline()
Твоя задача — объяснить, почему снова вернулась строка one.
Отдельно попробуй:
f.read()
f.read()
и посмотри, почему второй результат — ""."""

"""with open("file.txt","w", encoding="utf-8") as f:
    f.writelines("one\ntwo\nhree\nfour")
"""
"""with open("file.txt","r", encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())
    print(f.tell())
    print(f.readline())
    f.seek(0)
    print(f.readline())
"""
"""Ausgabe:
one

two

10
hree

one
"""
with open("file.txt","r", encoding="utf-8") as f:
    print(f.read())
    print(f.read())