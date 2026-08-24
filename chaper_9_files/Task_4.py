"""Задание 4 — чтение построчно
Создай users.txt:
Luka,20
Anna,25
Bob,31
Пройди файл:
for line in f:
Для каждой строки:
strip()
split(",")
и выведи примерно:
Name: Luka | Age: 20
Name: Anna | Age: 25
Name: Bob | Age: 31
Дополнительно преобразуй возраст из str в int"""
with open("users.txt", "w", encoding="utf-8") as f:
    f.write("Luka,20\n")
    f.write("Anna,25\n")
    f.write("Bob,31\n")

with open("users.txt","r",encoding="utf-8") as f:
    for line in f:
        line.strip()
        name, age = line.split(",")
        print(f"Name: {name} | Age: {age}")
        
"""
Name: Luka | Age: 20

Name: Anna | Age: 25

Name: Bob | Age: 31"""