import pdb
from random import randint


def test(n):
    pdb.set_trace()
    f = randint(1, n)
    return f * 2


if __name__ == "__main__":
    test(4)
