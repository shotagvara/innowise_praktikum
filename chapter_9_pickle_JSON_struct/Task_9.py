"""Задание 9 — сохранить packed data в настоящий файл
Упакуй два числа:
в bytes через struct.
Запиши их в:
image_info.bin
через:
"wb"
Потом отдельным открытием:
"rb"
прочитай файл и восстанови width и height.
То есть полный путь:
1920, 1080
     ↓
struct.pack
     ↓
bytes
     ↓
binary file
     ↓
read()
     ↓
bytes
     ↓
struct.unpack
     ↓
1920, 1080
Вот это очень полезное упражнение."""
import struct

width = 1920
height = 1080
data=struct.pack("ii",  width, height)

with open("image_info.bin", "wb") as f:
    f.write(data)

with open("image_info.bin", "rb") as f:
    data_2=f.read()

info = struct.unpack("ii", data_2)
print(info)
"""(1920, 1080)"""
print(info[0])