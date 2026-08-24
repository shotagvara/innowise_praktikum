"""Задание 7 — pack() / unpack()
Начни максимально просто:
import struct
number = 123
data = struct.pack("i", number)
Выведи:
data
type(data)
len(data)
Потом:
result = struct.unpack("i", data)
Выведи:
result
type(result)
Посмотри, почему результат:
(123,)
а не просто:
123
И вспомни singleton tuple."""
import struct
number = 123
data = struct.pack("i", number)
print(data)
print(len(data))
print(type(data))
result = struct.unpack("i", data)
print(result)
print(type(result))
"""b'{\x00\x00\x00'
4
<class 'bytes'>
(123,)
<class 'tuple'>"""