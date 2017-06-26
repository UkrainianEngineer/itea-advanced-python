def finger_name(number, fingers):
    number -= 1
    remainder = number % ((len(fingers) - 1) * 2)

    if remainder <= len(fingers) - 1:
        return fingers[remainder]

    if remainder > len(fingers) - 1:
        return fingers[len(fingers) - remainder - 2]
