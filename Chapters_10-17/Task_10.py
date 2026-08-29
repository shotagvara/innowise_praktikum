"""
10. Полиморфизм
    Напиши функцию:
def combine(a, b):
    ...
чтобы она просто использовала оператор +.
Проверь её минимум на трёх случаях:
combine(2, 3)
combine("Py", "thon")
combine([1, 2], [3, 4])
И объясни, почему одна функция работает со всеми тремя типами.
"""

def combine(a, b):
    return a+b


print(combine(2,3))
print(combine("Py","thon"))
print(combine([1,2],[3,4]))

"Works because python is polymorph language. There is no need to declare the types of variables like in java"