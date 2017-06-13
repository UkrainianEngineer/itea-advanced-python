mark = 0

def play_with_number(number, expected_value=None, expected_type=None):
    global mark
    print "Test for `{}`".format(number)
    eval_number = eval(number)
    print eval_number
    print type(eval_number)
    try:
        assert eval_number == expected_value, \
               "Wrong value for {}.".format(eval_number)
        assert isinstance(eval_number, expected_type), \
               "Wrong type for {}.".format(eval_number)
        mark += 1
    except AssertionError:
        print "Failed validations for {}.".format(number)
    print '=' * 60

play_with_number("1000000000000")
play_with_number("1 * 10e12")
play_with_number("1 + 2.0")
play_with_number("1.0 + 2")
play_with_number("1/2")
play_with_number("3/2")
play_with_number("-1/2")
play_with_number("-3/2")
play_with_number("3//2")
play_with_number("-3//2")
play_with_number("3**2")
play_with_number("9%4")

print "Final mark: {}.".format(mark)


print "Advanced part."
print "Bitwise operations."
def int_to_binary(number):
    return "{0:b}".format(number)

play_with_number("1>>2")
play_with_number("1<<2")
play_with_number("9>>2")

print int_to_binary(2)
print int_to_binary(9)


# Useful link:
# http://catbo.net/c/translated/Python-enru/Python.zip/tutorial/floatingpoint.html
