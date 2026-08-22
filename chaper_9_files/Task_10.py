"""Задание 10 — определить PNG без расширения
Переименуй копию:
image.png
в:
unknown_file
То есть убери расширение.
Напиши программу, которая не смотрит на имя файла, а читает первые 8 байтов и говорит:
This is a PNG file
если сигнатура совпала.
Это хороший пример того, почему:
binary data != filename extension"""

with open("unknown_file", "rb") as f:
    header=f.read(8)
    print(header)
    if "PNG" in str(header): 
        print(True)
    else: print(False)