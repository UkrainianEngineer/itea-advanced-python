data = {'a': 1, 'b': 2, 'c': 3}
print data
print data.keys()
print data.values()

def func(num):
    return sum(**num)

print func(**data)