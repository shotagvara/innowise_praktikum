"""Задание 1 — запись и чтение текста
Программа должна:

Создать notes.txt через "w" и encoding="utf-8".

Записать туда три строки:

Python
Innowise
Berlin
Закрытие сделать только через with, без ручного close().
Потом снова открыть файл и:
прочитать весь файл через read();
вывести результат;
вывести repr(result), чтобы увидеть \n."""

with open("notes.txt","w", encoding="utf-8") as f:
    f.write("Python\n")
    f.write("Innowise\n")
    f.write("Berlin\n")


with open("notes.txt","r", encoding="utf-8") as f:
    print(f.read())
    f.seek(0)
    print(repr(f.read()))