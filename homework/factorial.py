def fact1(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def fact2(n):
    f = 1
    while n > 0:
        f = f * n
        n -= 1
    return f

def fact3(n):
    return fact3(n)

print fact1(5)
print fact2(5)