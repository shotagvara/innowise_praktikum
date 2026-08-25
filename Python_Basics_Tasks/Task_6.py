"""Список как изменяемый объект — task06.py

languages = ["Python", "Java", "C++"]

Сделай последовательно:

1-добавь "JavaScript";
2-добавь "Rust" именно на вторую позицию;
3-измени "C++" на "C";
4-удали "Java";
5-выведи первый и последний элементы;
6-отсортируй список;
7-выведи его длину.

В отличие от предыдущего задания здесь объект должен изменяться на месте.
"""


#Что переделать:
#Объяснить почему ссылка поменялась и как этого избежать

languages = ["Python", "Java", "C++"]

#1
languages.append("JavaScript")
print(languages)


#2
languages.insert(1, "Rust")
print(languages)
print(id(languages))


#3-
"""Было"""
#languages=[lang.replace("C++","C") for lang in languages]
"""Здесь ссылка меняется потому, что у нас создаеься новый лист [], в который поместили обьекты старого листа с заменой"""


"""Стало Как можно сделать без замены ссылки:"""
index=languages.index("C++")
languages[index]="C"
print(id(languages))
print(languages)

#4
print(languages.remove("Java"))
print(languages)


#5
"""Was like this"""
print(languages[0], languages[-1])

"""не нашел как сделать кроме как так"""
first, *_ , last= languages
print(first, last) 

#6
languages.sort()
print(languages)

#7
print(len(languages))
