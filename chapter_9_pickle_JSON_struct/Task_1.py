"""Создай:
user
Преобразуй его через json.dumps().
Выведи результат.
Выведи type() результата.
Затем восстанови через json.loads().
Выведи тип восстановленного объекта.
Проверь:
user == restored

Ты должен руками увидеть:

dict
 ↓ dumps
str
 ↓ loads
dict"""
import json
user = {
    "name": "Luka",
    "age": 20,
    "active": True,
    "skills": ["Python", "Git"],
    "middle_name": None
}

text=json.dumps(user)
print(text)
print(type(text))

user_restored=json.loads(text)
print(type(user_restored))
print(user["skills"][0])