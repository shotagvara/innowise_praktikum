"""Задание 3 — вложенный JSON
Создай более реалистичную структуру:

Сохрани её в course.json, потом загрузи обратно.
После загрузки получи:
loaded["students"][0]["name"]
и:
loaded["students"][1]["score"]
Ожидаешь:
Anna
81
Тут ты одновременно повторишь dict + list + nested structures + JSON."""
import json
data = {
    "course": "Python",
    "students": [
        {
            "name": "Anna",
            "score": 92
        },
        {
            "name": "Bob",
            "score": 81
        }
    ],
    "completed": False
}
"""with open("course.json","w") as f:
    json.dump(data, f)"""

with open("course.json", "r") as f:
    loaded=json.load(f)

print(type(loaded))
print(loaded["students"][0])
print(loaded["students"][1])
"""
<class 'dict'>
{'name': 'Anna', 'score': 92}
{'name': 'Bob', 'score': 81}
"""