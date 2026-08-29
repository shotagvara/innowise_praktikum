"""
3. Цикл + continue + break
   Есть:
numbers = [3, -1, 8, 0, 12, -5, 20]
Напиши цикл, который:
- пропускает отрицательные числа;
- печатает положительные;
- полностью прекращает работу, когда встречает 0.
Не используй list comprehension.
"""

numbers = [3, -1, 8, 0, 12, -5, 20]

index=len(numbers)

for i in range(0,index):
    if numbers[i]>=0: 
        print(numbers[i])
    elif numbers[i]<0:
        continue
    else: break


