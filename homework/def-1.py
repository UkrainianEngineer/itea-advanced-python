a = 1
b = 2
c = 0

def func1(a, b):
	return a + b

def func2(foo, b):
	print foo(1, 2) + b

print func1(a, b)

func2(func1, b)

def func3(a, b):
	c = a - b
	return c

func3(a, b)
print c
print func3(a, b)

def func4(*args):
	return args

print func4(1, 2, 3)

def func5(kwargs):
	return kwargs.keys()

print func5({'a':1, 'b':2})