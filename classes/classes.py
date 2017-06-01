""" Brief description of the file:
Instances backer and smith made by classes Student and Teacher inherited from
Human.
These instances receive arguments during its creation.
Method "generate_dictionary" generates dictionary with numbers of elements
given during initialization of instance( by default = 2)
Method "generate_list_of_dictionaries" generates a list of dictionaries using
method mentioned above. This data is used for creating common_data which has to
be used for serialization.
Method serialize_info checks if attribute common_data exists in instance and
serializes result of above mentioned function and put it into common_data attr.
of instance.
Method file_writer writes common_data into appropriate file.
"""


import random
import string
import json
import pickle


class Human(object):
    def __init__(self, age, name, surname, gender, dict_element_nums=2,
                 list_of_dict_element_nums=2):
        self.age = age
        self.name = name
        self.surname = surname
        self.gender = gender
        self.dict_element_nums = dict_element_nums
        self.list_of_dict_element_nums = list_of_dict_element_nums

    def get_name(self, name):
        self.name = name

    def get_surname(self, surname):
        self.surname = surname

    def get_age(self, age):
        self.age = age

    def get_gender(self, gender):
        self.gender = gender

    def generate_dictionary(self, value_range=100, ):
        new_dict = {}
        for element in range(self.dict_element_nums):
            new_dict[random.choice(string.ascii_lowercase)] = (
                random.randint(1, value_range))
        return new_dict

    def generate_list_of_dictionaries(self, list_of_dict_element_nums=2):
        new_dict_list = []
        for element in range(list_of_dict_element_nums):
            new_dict_list.append(self.generate_dictionary())
        return new_dict_list


class Student(Human):
    def __init__(self, marks, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.marks = marks

    def get_average_mark(self):
        return float(sum(self.marks)) / len(self.marks)

    def serialize_info(self):
        self.common_data = json.dumps(self.generate_list_of_dictionaries
                                      (self.list_of_dict_element_nums))

    def file_writer(self):
        try:
            with open("json.txt", 'wb')as json_file:
                json_file.write(self.common_data)
        except AttributeError:
            self.serialize_info()
            self.file_writer()


class Teacher(Human):
    def __init__(self, classes, *args, **kwargs):
        super(Teacher, self).__init__(*args, **kwargs)
        self.classes = classes

    def get_number_of_classes(self):
        print(self.classes)

    def serialize_info(self):
        self.common_data = pickle.dumps(self.generate_list_of_dictionaries
                                        (self.list_of_dict_element_nums))

    def file_writer(self):
        try:
            with open("pickle.txt", 'wb')as pickle_file:
                pickle_file.write(self.common_data)
        except AttributeError:
            self.serialize_info()
            self.file_writer()


backer = Student([5, 4, 4, 4, 3, 3], 22, "Stephan", "Backer", "male", 7, 8)
smith = Teacher(32, 48, "Bob", "Smith", "male", 7, 10)

# backer.serialize_info()
# smith.serialize_info()

smith.file_writer()
backer.file_writer()
