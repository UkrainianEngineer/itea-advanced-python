General questions about Python and related topics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This document contains list of questions related to Python and similar topics.

Try to resolve all of them by yourself without google.


1. `sorted` vs `list.sort()`

>>> a = [1, -2, 4, 5, 0, 8, 11]
>>> sorted(a)
?
>>> a
?
>>> a.sort()
?
>>> a
?

2. What happened?

try:
    raise ValueError('Boom!')
except KeyError:
    print 'Got KeyError'
except Exception:
    print 'Got error'
except ValueError:
    print 'Got ValueError'

3. 1 + 1 == 2?
4. 1 + 1 is 2?
5. 1 + 2 == 3?
6. 1 + 2 is 3?
7. 256 + 1 == 257?
8. 256 + 1 is 257?
9. -7 + 1 == -6?
10. -7 + 1 is -6?

11. Calculate N factorial.
12. Reverse keys and values from dictionary. Example:

Input:

data = {"name": "Pavlo", "age": 27}

Output:

data = {"Pavlo": "name", 27: "age"}

13. Find min int value from list:
a = ['-1', '1', '4', '-9', '0']

Expected output:
-9

14. Show difference between mutable and immutable types in Python.

15. Show basic inheritance in Python.

16. Describe general architecture for school system, where are:
    - One teacher's computer
    - A lot of pupil's computers.
    Teacher should be able to install some specific programs into all pupil's
    computers.

17. What is JOIN in SQL? How it works? Types of JOINS?
18. What is `web server`?Which web servers do you know?
19. What is HTTP? Methods of HTTP.
20. Types of patterns? Tell something about your favourite pattern from each
    group.
21. How to integrate custom application with 3rd party API?
22. How to read file in real time in Linux?
23. Linux: kill all python processes.
24. What is SCRUM?
25. What is VCS? Proc and cons?
26. What is the reason of "send" method in Python's generators?
27. Add two dictionaries into one:

    first_dict = {"name": "Pavlo", "age": 27}
    second_dict = {"position": "teacher"}

28. Iterate through dictionary and print value of "age" key.
29. There are two huge lists. Return list of the same elements from both lists.

Example:
    list_one = [1,2,3,4,5,6,7,8,9, ...,100500, ...]
    list_second = [4, 11, 16, 100500, 'one', 'two', 'three', ...]

    Returns:
        [4, 11, 16, 10500]

30. Is it possible to open a few files using one `with` operator? Why?
31. We have the following data:
    ((id, name, score), (id, name, score), ...) 

    data = ((1, "Pavlo", 95), (2, "Stepan", 100), ...)

    a) Sort this data by id (ASCENDING)
    b) Sort this data by score (ASCENDING)
    c) Sort this data by name (DESCENDING)

All of these questions helps you to refresh your knowledge and to find your
gaps.
