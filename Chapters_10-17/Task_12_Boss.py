"""12. Мини-проект: счётчик через closure
    Напиши функцию:
def make_counter(start):
    ...
которая возвращает другую функцию.
Пример использования должен быть таким:
counter1 = make_counter(10)
counter2 = make_counter(100)

print(counter1())  # 11
print(counter1())  # 12
print(counter2())  # 101
print(counter1())  # 13
Условия:
- использовать вложенную функцию;
- использовать nonlocal;
- не использовать global;
- не использовать class.
Это задание проверяет сразу functions are objects + enclosing scope + closure + nonlocal.
Я бы делал их именно в таком порядке: 1–4 разогрев, 5–8 итерации и инструменты Python, 
9–12 функции и scope. Этого достаточно, чтобы нормально прогнать главы 10–17 без бессмысленного повторения одного и того же."""

def make_counter(start):
    counter=start

    def count():
        nonlocal counter
        counter+=1
        return counter

    return count

counter1= make_counter(10)
counter2= make_counter(100)
print(counter1())
print(counter1())
print(counter2())
print(counter1())
print(counter2())