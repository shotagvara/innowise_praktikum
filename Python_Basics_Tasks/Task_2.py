"""Строка как последовательность — task02.py
Дана строка:
language = "Programming Python"
Не создавая строк вручную, получи и выведи:
первый символ;
последний символ;
"Programming";
"Python";
первые 5 символов;
все символы кроме первых трёх;
строку наоборот;
длину строки."""
language = "Programming Python"

print(language[0])
print(language[-1])
print(language.split(" ")[0])

print(language.split(" ")[1])
print(language[:5])
print(language[3:])
print(language[::-1])
print(len(language))