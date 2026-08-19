"""
Список словарей — task12.py
Создай:

athletes = [
    {"name": "Alex", "weight": 80},
    {"name": "Max", "weight": 75},
    {"name": "John", "weight": 90}
]

Без циклов получи:

имя второго спортсмена;
вес третьего;
весь словарь первого спортсмена;
измени вес второго спортсмена на 77.

Это очень важное задание на понимание вложенности объектов."""
athletes=[
    {"name": "Alex", "weight":80},
    {"name": "Anton", "weight": 58},
    {"name": "Felix", "weight": 75}
]
print(athletes[1]["name"])
print(athletes[2]["weight"])
athletes[1]["weight"]=77
print(athletes)