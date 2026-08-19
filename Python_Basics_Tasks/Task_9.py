"""
Списковое включение — task09.py
Используй ту же matrix.

С помощью list comprehension получи:

[2, 5, 8]

То есть второй элемент каждой вложенной строки.

Потом получи список квадратов этих чисел:

[4, 25, 64]

Не делай это вручную.
"""
list=[]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(0,3):
    for j in range(0,3):
        if j==1: list.append(matrix[i][j])

print(list)

list=[a**2 for a in list]
print(list)