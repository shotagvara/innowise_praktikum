"""Задание 7 — создать настоящий binary file
Создай байты:
data = bytes([0, 1, 2, 65, 66, 67, 254, 255])
Запиши:
with open("data.bin", "wb") as f:
    ...
Потом прочитай через "rb".
Проверь:
type(data)
data[3]
data[3:4]
Ты должен получить принципиально:
65
b'A'
После этого ответь себе:
Почему data[3] — int, хотя data[3:4] — bytes?
"""
"""data = bytes([0, 1, 2, 65, 66, 67, 254, 255])
with open("data.bin", "wb") as f:
    f.write(data)
"""
with open("data.bin", "rb") as f:
    print(type(f.read()))
    f.seek(0)
    print(f.read()[3])
    f.seek(0)
    print(f.read()[3:4])
