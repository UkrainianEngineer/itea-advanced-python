"""This file describes simple tasks to be done at home by each student."""

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
# 2. Print name of the youngest one.
# 3. Print list of guys in range of 19-46 years old.
# 4. Print sum of ages of all members.
#    Result should be a sum of: 20 + 45 + 55 + 17.
# 5. Try to use filter, map, redure functions for 3rd task.

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

# 6*. Implement the 6th task without global variables.
# 
#    NOTE: you may get `2` more bonues points if you finish this task
#          till the next class.

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
