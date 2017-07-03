def generate():
    for value in [1, 2]:
        yield value

my_generator = generate()

print next(my_generator)  # 1
print next(my_generator)  # 2
print next(my_generator, 'End of iteration')  # End of iteration
print next(my_generator)  # Exception: StopIteration