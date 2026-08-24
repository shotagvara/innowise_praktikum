"""Финальное задание главы 9 — Binary Record
Сделай файл player.bin, в котором будет одна запись:
player_id = 42
wins = 15
weight = 83.5
Сам выбери подходящий format string из integer/float.
Программа №1:
Python values
→ struct.pack
→ player.bin
Программа №2:
player.bin
→ read bytes
→ struct.unpack
→ вывести:
ID: 42
Wins: 15
Weight: 83.5
А рядом сделай player.json с теми же данными.
После этого сравни своими словами:
player.json
vs
player.bin
по трём пунктам:
1. Можно ли прочитать глазами?
2. Нужно ли заранее знать структуру данных для чтения?
3. Что возвращает Python при обычном read() — str или bytes?"""
import json
import struct

player_id = 42
wins = 15
weight = 83.5
with open("player.bin", "wb") as f:
    f.write(struct.pack("iif", player_id, wins, weight))

player_data = {
    "player_id": player_id,
    "wins": wins,
    "weight": weight
}

with open("player.json", "w") as f:
    json.dump(player_data, f)

