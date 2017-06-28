data = {'a': 1, 'b': 2, 'c': 3}
print data
print data.keys()
print data.values()

def func(a, b, c):
    return a + b + c

print func(**data)