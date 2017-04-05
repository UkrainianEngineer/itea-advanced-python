"""This file describes simple tasks to be done at home by each student.

   Author: pivanchy.
"""
from random import randint

data = [
  {
    'name': 'Bob', 'age':20,
  },
  {
    'name': 'Martin', 'age': 45,
  },
  {
    'name': 'Steven', 'age': 55,
  },
  {
    'name': 'Kate', 'age': 17,
  },
]

# 1. Print name of the oldest one.

oldest = max(data, key=lambda x:x.get('age'))
print '=' * 60
print 'Name of the oldest is "%(name)s", age "%(age)d"' % oldest

# 2. Print name of the youngest one.

print '=' * 60
youngest = min(data, key=lambda x:x.get('age'))
print 'Name of the youngest is "%(name)s", age "%(age)d"' % youngest

# 3. Print list of guys in range of 19-46 years old.

in_range = [el for el in data if 19 < el.get('age') < 46]
print '=' * 60
print "List of guys in range of 19-46 years old: "
for guy in in_range:
    print '"%(name)s" is %(age)d years old.' % guy

# 4. Print sum of ages of all members.
#    Result should be a sum of: 20 + 45 + 55 + 17.

print '=' * 60
sum_of_ages = sum(element.get('age') for element in data)
print "Sum of ages: %d" % sum_of_ages

# 5. Try to use filter, map, redure functions for 3rd task.

candidates = map(lambda x: x if 19 < x.get('age') < 46 else None, data)
guys = filter(None, candidates)
print '=' * 60
print "Guys in range 19-46:"
for guy in guys:
    print '"%(name)s" is "%(age)d" years old.' % guy

# Additional tasks:

# 6. Implement function which counts number of its calls.
#
#    NOTE: you may get `2` bonus points if you finish this task
#          till the next class.
#
#    Examples of expected outputs:
#     print my_calls_counter() # prints 1
#     print my_calls_counter() # prints 2
#     print my_calls_counter() # prints 3
#     ...
#     etc.

# Simple solution:
counter = 0
def my_calls_counter():
    global counter
    counter += 1
    print counter

print '=' * 60
print "Funtion calls:"
my_calls_counter()
my_calls_counter()

# 6*. Implement the 6th task without global variables.
# 
#    NOTE: you may get `2` more bonues points if you finish this task
#          till the next class.

# Tricky solution:
def calls_counter(fn):
    counter = 0
    def wrapper():
        counter += 1
        print counter
    return wrapper

def my_calls_wrapper():
    pass

my_calls_wrapper = calls_counter(my_calls_wrapper)
print '=' * 60
print "Funtion calls:"
my_calls_counter()
my_calls_counter()

# 7. Let's to imagine next situation:
#
#    NOTE: you may get `5` bonus points if you finish this task
#          till the next class.
#
#    You have a list of file names with different extensions, like this:
#    list_of_files = ['reports.txt', 'monthly_reports.zip', 'README.txt',
#                     'picture.jpg', 'logo.ttf', 'config.ini']
#
#    For each type of files: TXT, ZIP, JPG, TTF, INI
#    You should create custom handler (function) which returns
#    random size of this file.
#    
#    You may use `random.randint`  from `random` module for generation
#    random size.
#    Example:
#        txt_handler(filename) # returns random number in range (100, 500)
#        zip_handler(filename) # returns random number in range(500, 700)
#        jpg_handler(filename) # returns random number in range(800, 1000)
#
#    Firstly, you must create a function to recognize type of file.
#    Example: 
#        recognize_file_type('reports.txt') # returns: txt
#        recognize_file_type('logo.ttf') # returnf ttf
#
#    Then, using `recognize_file_type` function you may create another function
#    which may execute your handlers for appropriate file.
#    Example:
#        run_executors(list_of_files) # execute `txt_handler` for .txt files,
#                                      `zip_handler` for .zip file, etc.
#
#    Finally, you may use `filter`, `map` or `reduce` functions for some cases.

list_of_files = ['reports.txt', 'monthly_reports.zip', 'README.txt',
                 'picture.jpg', 'logo.ttf', 'config.ini']

def txt_handler():
    return randint(100, 500)

def zip_handler():
    return randint(500, 700)

def jpg_handler():
    return randint(800, 1000)

def ttf_handler():
    return randint(1200, 2000)

def ini_handler():
    return randint(0, 100)

def handlers_mapping():
    return {'txt': txt_handler, 'zip': zip_handler,
            'jpg': jpg_handler, 'ttf': ttf_handler,
            'ini': ini_handler}

def get_handler(extension):
    mapped_objects = handlers_mapping()
    try:
        return mapped_objects[extension]
    except KeyError:
        print 'Unexpected extension "{}" found.'.format(extension)

def recognize_file_type(filename):
    """Return extension of file.

    Args:
        filename (str): name of file.

    Returns:
        str: extension of file in lowercase.
    """
    if '.' in filename:
        try:
            name, extension = filename.split('.')
        except ValueError:
            print 'Too many dots in file "%s".' % name
            # Get last extension of file as an original extension.
            extension = filename.split('.')[-1]
    return extension.lower()

def run_executors(list_of_files):
    for f in list_of_files:
        extension = recognize_file_type(f)
        handler = get_handler(extension)
        if handler:
            size_of_file = handler()
            print 'Size of "%s" file is "%s" bytes' % (f, size_of_file)
        else:
            print str('Can\'t calculate size for file with unknown'
                  ' extension "%s".' % extension)

print '=' * 60
# Make sure there is no empty strings in list.
list_of_files = filter(None, list_of_files)
run_executors(list_of_files)
