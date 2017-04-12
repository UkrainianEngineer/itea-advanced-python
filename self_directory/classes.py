class Human(object):
    def __init__(self, age, name, surname, gender):
        self.age = age
        self.name = name
        self.surname = surname
        self.gender = gender

    def get_name(self, name):
        self.name = name

    def get_surname(self, surname):
        self.surname = surname

    def get_age(self, age):
        self.age = age

    def get_gender(self, gender):
        self.gender = gender


class Student(Human):
    def __init__(self, marks, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.marks = marks

    def get_average_mark(self):
        return(float(sum(self.marks))/len(self.marks))


class Teacher(Human):
    def __init__(self, classes, *args, **kwargs):
        super(Teacher, self).__init__(*args, **kwargs)
        self.classes = classes

    def get_number_of_classes(self):
        print(self.classes)


backer = Student([5, 4, 4, 4, 3, 3], 22, "Stephan", "Backer", "male")
smith = Teacher(32, 48, "Bob", "Smith", "male")

print(backer.gender)
print(backer.marks)
print(backer.get_average_mark())

print(smith.surname)
print(smith.name)
smith.get_number_of_classes()
