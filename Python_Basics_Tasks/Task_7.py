"""
Строка vs список — task07.py
Создай:

string = "Python"
numbers = [1, 2, 3, 4, 5]

Сделай для обоих объектов:

len();
индекс [0];
индекс [-1];
срез [1:4];
* 2.
После этого в комментарии напиши своими словами: почему и строка, и список относятся к 
последовательностям, хотя один immutable, а второй mutable?
"""
string = "Python"
numbers = [1, 2, 3, 4, 5]
print(len(string), len(numbers))
print(string[0], numbers[0])
print(string[-1], numbers[-1])
print(string[1:4], numbers[1:4])
print(string*2, numbers*2)