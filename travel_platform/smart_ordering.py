data = [{'name': 'Pavlo', 'age': 27, 'gender': 'male'},
        {'name': 'Kate', 'age': 28, 'gender': 'female'},
        {'name': 'Duc', 'age': 48, 'gender': 'male'},
        {'name': 'Duc1', 'age': 48, 'gender': 'male'},
        {'name': 'Duc', 'age': 45, 'gender': 'male'},
        {'name': 'Sasha'},
        {'name': 'Sasha1'},
        {'name': 'Sasha2'},
        {'age': 60}, {'age': 10}, {'age': 20},
        {'name': 'Roman', 'gender': 'male'}]

def smart_ordering(data_dict, filter_by, limit=100):
    '''
    this function for sorting some list of dictionaries to given consistency
    '''
    if filter_by == 'name':
        sorted_data = sorted(data_dict, key=lambda note: note.get('name', 'z'))
    else:
        sorted_data = sorted(data_dict, key=lambda note: (note.get(filter_by, 'z'), note.get('name')))
    # return sorted_data[:limit]
    for note in sorted_data[:limit]:
        print note

print('Sorted by name:')
smart_ordering(data, 'name')
print('---'*15)
print('Sorted by age:')
smart_ordering(data, 'age')
print('---'*15)
print('Sorted by gender:')
smart_ordering(data, 'gender')
