def generate():
    for value in [1, 2]:
        yield value

gen = generate()

print generate()  # <generator object generate at 0x024301E8>
print next(generate())  # 1
print next(generate())  # 1
print next(generate())  # 1
print next(gen)  # 1
print next(gen)  # 2
print next(gen, 'end of iteration')  # end of iteration
print next(gen)  # exception: StopIteration
