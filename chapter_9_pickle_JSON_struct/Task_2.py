"""Задание 2 — dump() / load()
Тот же user сохрани в:
user.json
Используй:
with open(..., "w", encoding="utf-8")
и:
json.dump(...)
Потом открой файл через "r" и восстанови объект через:
json.load(...)

После выполнения открой user.json обычным текстовым редактором и посмотри, что там физически лежит.

Главный вопрос для себя:

Почему JSON-файл можно нормально прочитать глазами, а pickle-файл обычно нет?"""
import json
import pickle
user = {
    "name": "Luka",
    "age": 20,
    "active": True,
    "skills": ["Python", "Git"],
    "middle_name": None
}
"""with open("user.json","w", encoding="utf-8") as file:
    json.dump(user, file)
"""

with open("user.json", "r") as f:
    user_restored=json.load(f)

print(user_restored)
"""{'name': 'Luka', 'age': 20, 'active': True, 'skills': ['Python', 'Git'], 'middle_name': None}"""
print(type(user_restored))
"""<class 'dict'>"""
print(user_restored["skills"])

"""with open("user.pkl","wb") as f:
    pickle.dump(user, f)
"""
with open("user.pkl", "rb") as f:
    user_pickle=f.read()
    print(user_pickle)
"""b'\x80\x04\x95P\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x04Luka\x94\x8c\x03age\x94K\x14\x8c\x06active\x94\x88\x8c\x06skills\x94]\x94(\x8c\x06Python\x94\x8c\x03Git\x94e\x8c\x0bmiddle_name\x94Nu.'"""
print(pickle.loads(user_pickle))
"""{'name': 'Luka', 'age': 20, 'active': True, 'skills': ['Python', 'Git'], 'middle_name': None}"""
    