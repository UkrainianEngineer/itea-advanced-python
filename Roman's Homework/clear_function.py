def double(my_list):
    new_list =[]
    for element in my_list:
        new_list.append(element * 2)
    return new_list

our_list = [2, 4, 'Lviv']
print(our_list)
doubled_list = double(our_list)
print(doubled_list)
print(our_list)
