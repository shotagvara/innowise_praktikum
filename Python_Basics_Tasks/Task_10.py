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