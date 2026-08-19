"""Строковые методы — task05.py
Дана строка:

text = " python is simple, python is powerful  "

Не изменяя исходную строку вручную:

убери пробелы по краям;
замени python на Python;
посчитай количество Python;
найди позицию слова simple;
разбей строку на отдельные слова;
создай версию строки полностью в верхнем регистре.

После каждой операции выводи результат. Обрати внимание: исходный text изменился или нет?
"""
text = "  python is simple, python is powerful  "
print(text)
print(text.strip())
text=text.strip().replace("python", "Python")
print(text)
print(text.count("Python"))
print(text.find("simple"))
text1=text.split(" ")
for a in text1: 
    print(a)
print(text.upper())