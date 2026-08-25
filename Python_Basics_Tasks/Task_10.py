"""
Словарь — task10.py
Создай словарь спортсмена:


Затем:

выведи имя;
измени вес на 79;
увеличь количество побед на 1;
добавь ключ "country";
выведи все ключи;
выведи все значения;
удали "country";
проверь, существует ли ключ "age".
"""
athlete={
    "name": "Anton",
    "wins": 29,
    "weight": 30,
    "sport": "Boxing"
}
print(athlete["name"])
athlete["weight"]=79
print(athlete["weight"])
athlete["wins"]+=1
print(athlete)
athlete["country"]="Germany"
print(athlete)
print(athlete.keys())
print(athlete.values())
athlete.pop("country", None)
print(athlete)
print("age" in athlete)


"""DZ"""
print("DZ:")

foo= "age" in athlete
print(foo==0)  
print(False==0)
"foo равно False, пожтому получается False==0. А это истина, так как Фолс это и есть ноль на системном уровне "


print("age" in athlete == False)

"""
из-за цепочки сравнений (comparison chaining) Python разбил строку так:
("age" in athlete) and (athlete == False)


Согласно разделу официальной документации Python Language Reference — 6.10. Comparisons:
"Comparisons can be chained arbitrarily, e.g., x < y <= z is equivalent to 
x < y and y <= z..."

https://docs.python.org/3/reference/expressions.html#comparisons
"""
