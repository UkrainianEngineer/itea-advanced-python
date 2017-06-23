def finger_name(number, fingers):
    number -= 1
    remainder = number % ((len(fingers) - 1) * 2)

    if remainder <= (len(fingers) - 1):
        return fingers[remainder]

    if remainder > (len(fingers) - 1):
        return fingers[-(remainder - 3)]

# print finger_name(1, ['pinky', 'ring', 'middle', 'index', 'thumb'])
# print finger_name(12, ['pinky', 'ring', 'middle', 'index'])
