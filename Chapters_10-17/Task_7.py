"""7. Comprehension
   Из:
numbers = range(1, 11)
создай одним list comprehension список квадратов только нечётных чисел.
Ожидаемый смысл:
1, 9, 25, 49, 81"""

numbers = range(1, 11)

l=[x**2 for x in numbers if x%2!=0]
print(l)

"""
Output:
[1, 9, 25, 49, 81]

"""