"""Pickle
Задание 5 — первый .pkl
Создай:

Сохрани:
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
Загрузи:
with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)
Выведи:
loaded
type(loaded)
type(loaded["unique"])
type(loaded["point"])
Обрати внимание: pickle восстановит и:
set
tuple
которые обычный JSON напрямую не представляет."""
import pickle
data = {
    "name": "Luka",
    "numbers": [1, 2, 3],
    "unique": {10, 20, 30},
    "point": (5, 10)
}
"""with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
    """

with open("data.pkl", "rb") as f:
    loaded=pickle.load(f)

print(type(loaded))
print(type(loaded["unique"]))
print(type(loaded["point"]))
"""<class 'dict'>
<class 'set'>
<class 'tuple'>"""