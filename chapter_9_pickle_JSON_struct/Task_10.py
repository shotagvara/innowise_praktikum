"""Задание 10 — calcsize()
Посмотри:
struct.calcsize("i")
struct.calcsize("f")
struct.calcsize("if")
Сравни с:
len(struct.pack(...))
Твоя задача — понять:
format string определяет не только тип данных, но и размер ожидаемой binary-структуры."""
import struct

print(struct.calcsize("i"))
print(struct.calcsize("f"))
print(len(struct.pack("i", 42)))
print(len(struct.pack("f", 42.4)))