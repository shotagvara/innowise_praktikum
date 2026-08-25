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
    "name": "Alex",
    "physical": {
        "weight": 80,
        "hight": 190
    },
    "results": {
        "wins": 12,
        "loses": 3
    }
}
print(athlete["name"])
print(athlete["physical"]["hight"])
print(athlete["physical"]["weight"])
print(athlete["results"]["wins"])
print(athlete["results"]["loses"])
athlete["results"]["wins"]+=1
print(athlete)

"""
Alex
190
80
12
3
{'name': 'Alex', 'physical': {'weight': 80, 'hight': 190}, 'results': {'wins': 13, 'loses': 3}}
PS C:\Users\Amstel\Desktop\Innowise Praktikum> 
"""