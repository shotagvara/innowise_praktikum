"""Задание 6 — equality vs identity после pickle
Возьми:
original = {
    "numbers": [1, 2, 3]
}
Сохрани и загрузи его в loaded.
Проверь:
original == loaded
original is loaded
А потом:
original["numbers"] is loaded["numbers"]
Перед запуском попробуй предсказать результаты.
Задача здесь очень хорошая: она связывает pickle с нашей старой темой:
== vs is
objects
references"""
import pickle
original = {
    "numbers": [1, 2, 3]
}
with open("original.pkl","wb") as f:
    pickle.dump(original, f)

with open("original.pkl", "rb") as f:
    loaded=pickle.load(f)

print("original==loaded: ", original==loaded)
print("original is loaded: ", original is loaded)
print(loaded["numbers"] is original["numbers"])
"""original==loaded:  True
original is loaded:  False
False"""