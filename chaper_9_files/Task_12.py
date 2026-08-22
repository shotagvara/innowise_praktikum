"""Задание 12 — копирование файла кусками
Теперь запрещено делать:
data = source.read()
всего файла.
Читай, например, по:
1024
байта.
Логика:
read chunk
↓
write chunk
↓
read next chunk
↓
...
И остановись, когда read() вернёт пустой bytes:
b""
Это симуляция того, как работать с очень большими файлами, не загружая всё содержимое в RAM."""
with open("image.png","rb") as file, open("copy.png","wb") as c:
    while True:
        line=file.read(1024)
        if not line: break
        c.write(line)