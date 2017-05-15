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


def smart_ordering(data_dict, filter_by=None, order_by='ASC', limit=100):
    '''
    Sorting data by different conditions.
    Args:
        data (list): List of dictionaries with data to sort.
        filter_by (str): Filtering attribute.
        order_by (str:ASC|DESC): Filtering order.
        limit (int): Limitation of data to return.

    Returns:
        list: Sorted list of dictionaries with applied filters.
    '''
    order_by = order_by.upper()

    if filter_by is None:
        return sorted(data_dict)

    if order_by == 'DESC':
        sorted_data = sorted(data_dict,
                             key=lambda note: (filter_by not in note,
                                               note.get(filter_by)),
                             reverse=True)
    else:
        sorted_data = sorted(data_dict,
                             key=lambda note: (filter_by not in note,
                                               note.get(filter_by)))


    return sorted_data[:limit]