data = [{'name': 'Pavlo', 'age': 27, 'gender': 'male'},
        {'name': 'Kate', 'age': 28, 'gender': 'female'},
        {'name': 'Duc', 'age': 48, 'gender': 'male'},
        {'name': 'Duc1', 'age': 48, 'gender': 'male'},
        {'name': 'Duc', 'age': 45, 'gender': 'male'},
        {'name': 'Sasha'},
        {'name': 'Sasha1'},
        {'name': 'Sasha2'},
        {'age': 60},
        {'age': 10},
        {'age': 20},
        {'name': 'Roman', 'gender': 'male'}]

sorted_data = filter(lambda note: not note.get('age'), data)
# sorted_data = sorted(data_dict, key=lambda note:
#                     (filter_by not in note if order_by.lower() == "asc"
#                      else filter_by in note, note.get(filter_by)),
#                      reverse=True if order_by.lower() == 'desc' else False)

print sorted_data
