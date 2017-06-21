def func1(*args):
    print(args)

def func2(**kwargs):
    print(kwargs)

def func3(**kwargs):
    for k in kwargs.keys():
        print k,
    for v in kwargs.values():
        print v

func1(1, 2, 3)   # (1, 2, 3) - tuple

func2(a=1, b=2, c=3)  #  {'a': 1, 'c': 3, 'b': 2} - dict

# func3(a=1, b=2, c=3)  #  a c b 1 3 2

def func4(kwargs):
    for i in kwargs:
        print i

kwargs = {'a': 1, 'b': 2, 'c': 3}
func4(kwargs)
