"""Финальное задание главы — task15.py
Создай маленькую базу данных боксёров:

Программа должна получить из этой структуры и вывести вес Alex, победы John и поражения Max. 
 Затем увеличить победы Alex на одну, добавить нового боксёра, вывести список всех имён боксёров 
 и сохранить строковое представление всей структуры в boxers.txt.

Бонус: с помощью for выведи каждого боксёра и его данные отдельно. 
Это уже чуть сложнее, но цикл for Лутц кратко показывает в этой главе при работе со словарями."""
boxers = {
    "Alex": {
        "weight": 80,
        "wins": 12,
        "losses": 3
    },
    "John": {
        "weight": 75,
        "wins": 8,
        "losses": 1
    },
    "Max": {
        "weight": 86,
        "wins": 15,
        "losses": 5
    }
}
print(boxers["Alex"]["weight"])
print(boxers["John"]["wins"])
print(boxers["Max"]["losses"])
boxers["Alex"]["wins"]+=1
boxers.update({"New one": {
    "weight": 86,
    "wins": 15,
    "losses": 5}})
print(boxers.keys())

file=open("boxers.txt", "w")
file.write(str(boxers))
file.close()

for boxer, data in boxers.items():
    print(f"{boxer}: {data}")