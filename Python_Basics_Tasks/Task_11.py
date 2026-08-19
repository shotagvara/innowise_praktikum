"""Вложенный словарь — task11.py
Создай структуру:


Используя только обращения по ключам, выведи:

Alex
190
80
12
3

Затем измени количество побед на 13."""

athlete= {
    "name": "Anton",
    "physical": {
        "weight": 80,
        "hight": 182
    },
    "results": {
        "wins": 20,
        "loses": 10
    }
}
print(athlete["name"])
print(athlete["physical"]["weight"])
print(athlete["results"]["wins"])
print(athlete["results"]["loses"])
athlete["results"]["wins"]+=1
print(athlete)