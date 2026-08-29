"""11. LEGB / global / nonlocal
    Сначала не запускай, а предскажи вывод:
    Потом запусти и объясни, какой x меняется на каждом уровне.
"""

x = 100

def outer():
    x = 10

    def inner():
        nonlocal x
        x += 5
        "line 9 x changes, when inner() executes"
        print("inner:", x)
        

    inner()
    "inner() executes -> from x from line 9 beckomes 15"
    print("outer:", x)

outer()
print("global:", x)


"global x from line 6 prints"



"""  My opinion(is true):
inner: 15
outer: 15
global: 100

"""
                                                                                                                                                                                                                                                                           