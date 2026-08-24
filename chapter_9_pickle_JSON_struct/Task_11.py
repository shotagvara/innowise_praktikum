"""Endianness
Задание 11 — одни данные, разные bytes
Возьми:
number = 0x12345678
Создай:
big = struct.pack(">I", number)
little = struct.pack("<I", number)
Выведи:
big.hex()
little.hex()
Ты должен увидеть байты примерно в обратном порядке.
Потом распакуй каждый правильным форматом:
struct.unpack(">I", big)
struct.unpack("<I", little)
И получи исходное число.
Главная цель:
одно число
но разный byte order"""
import struct
number = 0x12345678
big = struct.pack(">I", number)
little = struct.pack("<I", number)
print(big.hex())
print(little.hex())
big_unpacked=struct.unpack(">I",big)
little_unpacked=struct.unpack("<I", little)
print(big_unpacked)
print(little_unpacked)
