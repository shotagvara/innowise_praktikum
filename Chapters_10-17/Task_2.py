"""2. Найди ошибку в условии
   Исправь код:
answer = input("Continue? ").strip().lower()

if answer == "yes" or "y":
    print("Continue")
else:
    print("Stop")
И объясни, почему исходный вариант работает неправильно."""



answer = input("Continue? ").strip().lower()


"""
if answer == "yes" or "y" 
Выдает всегда тру, так как (or y) true
"""

if answer in ["yes", "y"]:
    print("Continue")
else:
    print("Stop")
