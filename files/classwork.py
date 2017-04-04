"""This module describes how to work with
   data serialization-deserialization.

   Author: pivanchy.
"""

import json
import pickle

data = {"username": "pivanchy", "name": "Pavlo", "age": 27}

def get_serialized_data(raw_data, data_format='pickle'):
    if data_format == 'pickle':
        return pickle.dumps(raw_data)
    return json.dumps(raw_data)

def get_deserialized_data(serialized_data, data_format='pickle'):
    if data_format == 'pickle':
        return pickle.loads(serialized_data)
    return json.loads(serialized_data)

serialized_data = get_serialized_data(data)
print "Pickle: Serialized data: %s" % serialized_data

deserialized_data = get_deserialized_data(serialized_data)
print "Pickle: Deserialized data: %s" % deserialized_data


# Working with file

filename = '/tmp/serialization'

def use_files(filename, data_format="pickle"):
    with open(filename, 'wb') as fin:
        # Use `wb` mode for binary writing.
        # Dump serialized data into file.
        if data_format == "pickle":
            pickle.dump(data, fin)
        json.dump(data, fin)

    with open(filename, 'rb') as fout:
        # Use `rb` mode for binary reading.
        # Load serialized data from file.
        if data_format == "pickle":
            deserialized = pickle.load(fout)
        deserialized = json.load(fout)
        print "Read from file: %s" % deserialized


# JSON

serialized_data = get_serialized_data(data, data_format='json')
print "JSON: Serialized data: %s" % serialized_data

deserialized_data = get_deserialized_data(serialized_data, data_format='json')
print "JSON: Deserialized data: %s" % deserialized_data

#use_files(filename, data_format="pickle")
#use_files(filename, data_format="json")
