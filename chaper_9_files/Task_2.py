"""Используй тот же notes.txt.
Сначала открой через:
"a"
и добавь:
Append works
Проверь содержимое.
Потом открой через:
"w"
и запиши только:
New file
После этого своими словами объясни, почему старые четыре строки исчезли."""

with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Append works\n")

with open("notes.txt","r", encoding="utf-8") as f:
    for line in f:
        print(line)

        
"""Ausgabe:
Python

Innowise

Berlin

Append works
"""
with open("notes.txt","w", encoding="utf-8") as f:
    f.write("New file")

with open("notes.txt","r", encoding="utf-8") as f:
    print(f.read())

"""Ausgabe:
New file
"""