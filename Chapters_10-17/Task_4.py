"""
4. range, enumerate, zip
   Есть:
names = ["Anna", "Bob", "Max"]
scores = [82, 91, 76]
Выведи:
1. Anna: 82
2. Bob: 91
3. Max: 76
Постарайся сделать это одним for, используя одновременно enumerate() и zip().
"""

names = ["Anna", "Bob", "Max"]
scores = [82, 91, 76]

for name, score in enumerate(zip(names, scores), start=1):
    print(name, score)

for name in enumerate(names):
    print(name)