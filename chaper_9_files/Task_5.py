"""Задание 5 — Unicode и UTF-8
Возьми строку:
text = "Привет | Berlin | თბილისი | €"
Сделай:
encoded = text.encode("utf-8")
Выведи:
text
type(text)
encoded
type(encoded)
Потом:
decoded = encoded.decode("utf-8")
И проверь:
decoded == text
Должно быть:
True
Главная цель — руками увидеть:
str
 ↓ encode
bytes
 ↓ decode
str
Это продолжает модель из главы 7 и файловой модели главы 9"""
text = "Привет | Berlin | თბილისი | €"
encoded= text.encode("utf-8")
print(encoded)
decoded= encoded.decode("utf-8")
print(decoded)
print(decoded==text)