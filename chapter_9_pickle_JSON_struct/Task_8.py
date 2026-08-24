"""Задание 8 — несколько значений
Упакуй:
age = 20
weight = 83.5
например через формат:
"if"
Потом распакуй обратно.
Цель:
int + float
    ↓ pack
bytes
    ↓ unpack
tuple(int, float)"""
import struct
data = struct.pack("if", 20, 83.5)
print(data)
data_unpacked=struct.unpack("if", data)
print(data_unpacked[1])