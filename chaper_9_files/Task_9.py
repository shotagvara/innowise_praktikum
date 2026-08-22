import timg
"""Задание 9 — работа с настоящим PNG
Возьми любой .png файл, скопируй его в папку проекта как:
image.png
Открой:
with open("image.png", "rb") as f:
Прочитай только первые 8 байт:
header = f.read(8)
Выведи:
header
header.hex()
Для PNG начало должно соответствовать сигнатуре:
b"\x89PNG\r\n\x1a\n"
Проверь:
header == b"\x89PNG\r\n\x1a\n"
Если это нормальный PNG, ожидаешь True.
Вот здесь ты уже буквально используешь binary I/O для определения формата файла по его содержимому."""
with open("image.png", "rb") as f:
    header=f.read(20)
    print(header)
    print(header.hex())
    f.seek(0)
timg.Rederer().render_image("image.png")
    
