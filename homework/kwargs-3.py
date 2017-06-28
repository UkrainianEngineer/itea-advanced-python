def var_args_call(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

kwargs = {"arg3": 3, "arg2": "two"}
var_args_call(1, **kwargs)

def func(a, b, c):
    print "a =", a
    print "b =", b
    print "c =", c

kwargs = {"a": 1, "b": 2, "c": 3}
func(**kwargs)