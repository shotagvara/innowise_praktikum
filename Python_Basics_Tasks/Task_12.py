"""
Список словарей — task12.py
Создай:

athletes = [
    {"name": "Alex", "weight": 80},
    {"name": "Max", "weight": 75},
    {"name": "John", "weight": 90}
]

Без циклов получи:

#1 имя второго спортсмена;
#2 вес третьего;
#3 весь словарь первого спортсмена;
#4 измени вес второго спортсмена на 77.

Это очень важное задание на понимание вложенности объектов."""
athletes = [
    {"name": "Alex", "weight": 80},
    {"name": "Max", "weight": 75},
    {"name": "John", "weight": 90}
]

#1
print(athletes[1]["name"])

"""Max"""

#2
print(athletes[2]["weight"])

"""90"""

#3
print(athletes[0])
"""{'name': 'Alex', 'weight': 80}"""

#4
athletes[1]["weight"]=77