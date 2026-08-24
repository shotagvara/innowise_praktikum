"""
Задание 4 — тип, который JSON не понимает
Попробуй:
data = {
    "numbers": {1, 2, 3}
}
и:
json.dumps(data)
Посмотри ошибку.
Потом исправь структуру так, чтобы её можно было сохранить в JSON.
Например, подумай, во что логично преобразовать set.
Цель — самому увидеть:
Python types
        ≠
JSON types"""
import json
data = {
    "numbers": {1, 2, 3}
}
"""with open("numbers.json","w") as f:
    json.dumps(data)
    """
"""TypeError: Object of type set is not JSON serializable"""
data2= {
    "numbers": [1,2,3]
}

with open("numbers.json","w") as f:
    json.dump(data2, f)

with open("nos.json","w") as f:
    string=json.dumps(data2) 
print(string)