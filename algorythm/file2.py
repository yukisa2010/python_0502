def add(a,b):
    return a + b

print(add(1,2))

def calc(a,b):
    x1 = a + b
    x2 = a - b
    x3 = a * b
    x4 = a / b
    return x1, x2, x3, x4

print(calc(2,3))

def exchange(a,b):
    tmp = a
    a = b
    b = tmp
    return (a,b)

print(exchange(2,5))

# リストの和

def add2(a,b):
    c = []
    for (_a,_b) in zip(a,b):
        c.append(_a + _b)
        
    return c

print(add2([1,2,3],[4,5,6,7]))

