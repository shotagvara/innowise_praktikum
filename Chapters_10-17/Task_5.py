"""5. Iterator руками
   Не используя for, выведи все элементы:
data = ["A", "B", "C"]
через:
iter()
next()
И специально вызови next() ещё один раз после конца, чтобы увидеть, какое исключение появляется.
"""
data = ["A", "B", "C"]

"creates iterator for object data"
iterator=iter(data)

for i in range(0, len(data)):
        print(next(iterator))
    

"Feheler tritt auf: StopIteration"


"""How to catch exception"""
for i in range(0,len(data)+1):
        try: 
               print(next(iterator))
        except: StopIteration