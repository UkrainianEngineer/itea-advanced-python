"""
Example of using composition instead of inheritance
"""


class Learner:
    def __init__(self):
        self.classes = []

    def enrol(self, course):
        self.classes.append(course)


class Teacher:
    def __init__(self):
        self.courses_taught = []

    def assign_teaching(self, course):
        self.courses_taught.append(course)


class Person:
    def __init__(self, name, surname, number, learner=None, teacher=None):
        self.name = name
        self.surname = surname
        self.number = number
        #add behaviours as attrubutes insted of inheritance
        self.learner = learner
        self.teacher = teacher

    def enrol(self, course):
        if not hasattr(self, "learner"):
            raise NotImplementedError()

        self.learner.enrol(course)

    def assign_teaching(self, course):
        if not hasattr(self, "teacher"):
            raise NotImplementedError()

        self.teacher.assign_teaching(course)

jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())
jane.enrol("Mathematics")
print(jane.learner.classes)
