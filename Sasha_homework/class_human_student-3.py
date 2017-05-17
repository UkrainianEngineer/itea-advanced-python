import json
import random
import string

class Humans(object):
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

user = Humans('Nicolas', 'Cage', 53, 'man')

print('username: ' + str(user.get_name()))
print(str(user.get_name()) + ' is %d years old' %(user.get_age()))

class Students(Humans):
    def __init__(self,  list_marks, *args, **kwargs):
        super(Students, self).__init__(*args, **kwargs)
        self.list_marks = list_marks

    def get_average_mark(self):
        return float(sum(self.list_marks)) / len(self.list_marks)

student_a = Students([5, 10, 6, 9, 8, 10, 7, 2, 1, 4],
                    'Alec', 'Baldwin', '59', 'man')

print('the student_a name is ' + str(student_a.get_name()))
print ('average mark for student %s is: ' +
       str(student_a.get_average_mark()))\
       %(student_a.get_name())

class Teachers(Humans):
    def __init__(self, group, *args):
        super(Teachers, self).__init__(*args)
        self.group = group

    def get_number_group(self):
        return self.group

teacher_a = Teachers('1-A', 'Sandra', 'Bullock', '52', 'woman')

print('the teacher_a name is ' + str(teacher_a.get_name()))
print ('the teacher %s is from ' +
       str(teacher_a.get_number_group()) + ' class')\
       %(teacher_a.get_name())

print('--' * 25)

def random_data():
    ''' This function return dictionary of random data for human: name, surname, age, gender '''
    data = {}
    list_upper_case = list(string.uppercase)
    list_lower_case = list(string.lowercase)
    apper_leter = random.choice(list_upper_case)
    apper_leter_2 = random.choice(list_upper_case)
    lower_letters = reduce(lambda x, y: x + y, random.sample(list_lower_case, 3))
    lower_letters_2 = reduce(lambda x, y: x + y, random.sample(list_lower_case, 5))
    data['name'] = apper_leter + lower_letters
    data['surname'] = apper_leter_2 + lower_letters_2
    data['age'] = random.randint(16, 60)
    data['gender'] = random.choice(['man', 'women'])
    return data

# create file with random data for 100 student
with open('students.json', 'w') as my_file:
    # quantity of student == 100
    data_base_students = [random_data() for i in range(100)]
    my_file.write(json.dumps(data_base_students))

with open('students.json', 'r') as my_file:
    data_base_students = json.loads(my_file.read())

# random marks
marks = [random.randint(0, 10) for mark in range(10)]

def stud_info(data_student):
    ''' This function recives random data for 'Student' and returns information about it.
     data_stud == data_base_students[x]
    '''
    student = Students(marks,
                       data_student['name'],
                       data_student['surname'],
                       data_student['age'],
                       data_student['gender'])
    return student

number_stud = random.randint(0, 99)
print(data_base_students[number_stud])
print('student #%d name is '
      + str(stud_info(data_base_students[number_stud]).get_name()))\
      % number_stud
print(str(stud_info(data_base_students[number_stud]).get_surname())
      + ' is ' +
      str(stud_info(data_base_students[number_stud]).get_gender()))
print("the surname student's %s is "
      + str(stud_info(data_base_students[number_stud]).get_surname()))\
      % str(stud_info(data_base_students[number_stud]).get_name())
print('%s is %d years old')\
      % (str(stud_info(data_base_students[number_stud]).get_name()),\
        stud_info(data_base_students[number_stud]).get_age())
print('marks: ' + str(marks))
print('average mark: ' + str(stud_info(data_base_students[number_stud]).get_average_mark()))