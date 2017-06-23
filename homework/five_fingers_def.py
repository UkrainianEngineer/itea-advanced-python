def finger_name(number, fingers):
    number -= 1
    remainder = number % ((len(fingers) - 1) * 2)

    if remainder <= (len(fingers) - 1):
        print 'first case: ', fingers[remainder]

    if remainder > (len(fingers) - 1):
        print 'second case: ', fingers[-(remainder - 3)]

# finger_name(1, ['pinky', 'ring', 'middle', 'index', 'thumb'])
# finger_name(8, ['pinky', 'ring', 'middle', 'index'])
