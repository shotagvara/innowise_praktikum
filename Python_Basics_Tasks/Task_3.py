"""Операции над последовательностями — task03.py
Даны:
a = "Python"
b = "Java"

Получи новую строку:

PythonJavaPythonJavaPythonJava

Используй только + и *.
Затем проверь с помощью in, содержатся ли "thon" и "C++" в получившейся строке.
"""
a = "Python"
b = "Java"
c=(a+b)*3
print(c)
print("thon" in c)
print("C++" in c)