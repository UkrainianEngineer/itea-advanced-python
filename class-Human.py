# FIRST change for github


class Human:
    
    def __init__(self):
        print('The super class is "Human" ')
        name = ""
        surname = ""
        age = 0
        gender = ""
    
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender

class Student(Human):

    marks = []  #list of student's marks
    
    def __init__(self):
        print('Object of class "Student" is created')
        super().__init__()
    
    def get_average_mark(self):
        sum = 0 
        for mark in self.marks:
            sum += mark
            average_mark = sum/len(self.marks)
        return average_mark

class Teacher(Human):
    
    classes = 0
    
    def __init__(self):
        print('Object of class "Teacher" is created')
        super().__init__()

    def get_number_of_classes(self):
        return self.classes   
    
# Student's instance:

student_1  = Student()
student_1.name = 'Igor'
print('Student_1\'s name is : ' ,student_1.get_name())

student_1.marks.append(5)
student_1.marks.append(6)
student_1.marks.append(7)
print('Student_1\'s marks are : ',student_1.marks)
print('and his average mark is : ',student_1.get_average_mark())
print()

# Teacher's instance:

teacher_1  = Teacher()
teacher_1.age= 35
teacher_1.classes = 5
print('teacher_1\'s age is : ' ,teacher_1.get_age())
print('He has : ' ,teacher_1.get_number_of_classes(), 'classes')


