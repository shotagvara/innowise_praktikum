"""Список как изменяемый объект — task06.py

languages = ["Python", "Java", "C++"]

Сделай последовательно:

добавь "JavaScript";
добавь "Rust" именно на вторую позицию;
измени "C++" на "C";
удали "Java";
выведи первый и последний элементы;
отсортируй список;
выведи его длину.

В отличие от предыдущего задания здесь объект должен изменяться на месте.
"""
languages = ["Python", "Java", "C++"]
print(type(languages))
languages.append("JavaScript")
print(languages)
languages.insert(1, "Rust")
print(languages)
languages=[lang.replace("C++","C") for lang in languages]
print(languages)
print(languages.remove("Java"))
print(languages)
print(languages[0], languages[-1])
languages.sort()
print(languages)
print(len(languages))
