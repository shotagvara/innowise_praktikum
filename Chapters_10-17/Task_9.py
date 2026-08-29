"""
9. return vs print()
   Исправь функцию так, чтобы следующий код работал:
def multiply(a, b):
    print(a * b)

result = multiply(4, 5)
print(result + 10)
После исправления должно напечататься:
30
"""


def multiply(a, b):
    return(a * b)

result = multiply(4, 5)
print(result + 10)

"Becasue the function has to return and not to print the result"