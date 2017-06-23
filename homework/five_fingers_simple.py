fingers = ['pinky', 'ring', 'middle', 'index', 'thumb']
number = 4
remainder = number % 8

if remainder <= 4:
    print fingers[remainder]

if remainder > 4:
    print fingers[-(remainder - 3)]
