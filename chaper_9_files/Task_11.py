"""Задание 11 — binary copy
Возьми image.png.
Напиши программу:
image.png
     ↓
Python
     ↓
image_copy.png
Используй:
"rb"
"wb"
После копирования сравни:
original_data == copied_data
Должно быть:
True
Ещё сравни:
len(original_data)
len(copied_data)
Одинаковы ли размеры?"""
with open("image.png", "rb") as f:
    data= f.read()

with open("image_copy.png", "wb") as f:
    f.write(data)




