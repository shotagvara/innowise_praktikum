"""1. Expression vs statement + input()
   Напиши программу, которая спрашивает у пользователя возраст и печатает:
   - "minor", если меньше 18;
   - "adult", если 18–64;
   - "senior", если 65+.
Условия:
input()
int()
if / elif / else"""


"Enters age as string and casts to int"
age=int(input("Age: "))


if age<18: 
    print("minor")
elif age<=64:
    print("adult")
else: print("senior")
