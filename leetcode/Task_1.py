""" You are given two non-empty  lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Constraints:
The number of nodes in each list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
list1= [2,4,3]
list2= [5,6,4]

print(list1[::-1])


def list_reverse_to_number(list):
    b=""
    for x in list[::-1]:
        b+=str(x)
    return int(b)

def two_lists(list1, list2) -> list:
    number=list_reverse_to_number(list1)+list_reverse_to_number(list2)
    if number==0:
        return [0]
    list=[]
    while number!=0:
        list.append(number % 10)
        number=number//10
    return list

print(list_reverse_to_number(list1))
print(list_reverse_to_number(list2))
print(two_lists(list1, list2))
print(two_lists([9,9,9,9,9,9,9],[9,9,9,9]))
print(two_lists([0],[0]))

# Gemini
def add_two_numbers_lists(l1: list, l2: list) -> list:
    result = []
    carry = 0
    i, j = 0, 0
    
    # Итерируемся, пока не пройдем оба списка или пока остался перенос
    while i < len(l1) or j < len(l2) or carry:
        # Берем цифру из списка, если индекс не вышел за границы, иначе 0
        val1 = l1[i] if i < len(l1) else 0
        val2 = l2[j] if j < len(l2) else 0
        
        # Считаем сумму текущего разряда и переноса
        total = val1 + val2 + carry
        carry = total // 10       # Новый перенос (0 или 1)
        result.append(total % 10) # Записываем остаток в результат
        
        # Двигаем указатели вперед
        i += 1
        j += 1
        
    return result

# Проверка примера 1:
print(add_two_numbers_lists([2, 4, 3], [5, 6, 4]))  # Выведет: [7, 0, 8]


#method 2

def add_two_numbers_pythonic(l1: list, l2: list) -> list:
    # 1. Разворачиваем списки и превращаем цифры в строки: ['3', '4', '2']
    str1 = [str(x) for x in l1[::-1]]
    str2 = [str(x) for x in l2[::-1]]
    
    # 2. Склеиваем строки и превращаем в целые числа: 342 + 465 = 807
    num1 = int("".join(str1))
    num2 = int("".join(str2))
    total = num1 + num2
    
    # 3. Превращаем сумму в строку, разворачиваем и делаем списком чисел
    return [int(x) for x in str(total)][::-1]

# Проверка примера 3:
print(add_two_numbers_pythonic([9,9,9,9,9,9,9], [9,9,9,9]))  # Выведет: [8, 9, 9, 9, 0, 0, 0, 1]
