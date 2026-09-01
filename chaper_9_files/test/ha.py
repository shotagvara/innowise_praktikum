"""
Benchmark. Сравни через timeit два способа получить квадраты чисел 0..9999: list comprehension и map. 
Прогони каждый вариант много раз и выведи оба времени. После этого одной фразой в комментарии напиши, 
какой оказался быстрее на твоём компьютере.
 Это как раз практическое закрепление главы 21; в книге эта глава посвящена timing/benchmarking и timeit."""

import timeit 


# Передаем код в виде строки
list_time = timeit.timeit("[x**2 for x in range(0, 10000)]", number=10000)
print(f"Время выполнения list: {list_time:.4f} секунд")

map_time = timeit.timeit("list(map(lambda x: x**2, range(100)))")
print(f"Время выполнения map: {map_time:.4f} секунд")
