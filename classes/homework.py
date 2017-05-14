#  1)  Create base `Human` class with following fields:
#      `name`, `surname`, `age`, `gender`
#
#      Also add following methods:
#      `get_name`, `get_username`, `get_age`, `get_gender`
#      All of these methods should return values of appropriate fields.
#
#      Create class `Student` inherited from (based on) `Human` class.
#      `Student` class should have `marks` field as a list of their marks.
#      Also add `get_average_mark` method to this class.
#      It should calculate average mark for student.
#
#      Create class `Teacher` inherited from (based on) `Teacher` class.
#      `Teacher` class should have `classes` field
#      as a number of teacher's classes.
#      Also please add `get_number_of_classes` method to this class.
#
#      Create instance of each class, fill class data,
#      use appropriate methods of classes.
#
#
#  2) Extend first program. Add next improvements:
#
#     - Add separate function to generate a lot of data (e.g. list of thousands
#       dictionaries with some random data).
#     - Add some logic to save a serialized data into file.
#     - Student class should be associated with `json` type somehow
#       (via specific field or specific implementation for data serialization).
#     - Teacher class should be associated with `pickle` type somehow
#       (via specific field or specific implementation for data serialization).
#     - Make it easy extensible for a new class with a new data type.
