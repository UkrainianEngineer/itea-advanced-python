"""This file describes simple tasks to be done at home
   using loops and built-in funtions.

   Author: pivanchy.
"""

testing_list = [1, 2, 3, 4, 0, -1, 4, 5, 6, 7, 8, 9]

# 1. Find minimal element of list using `for` loop.

minimal = testing_list[0]

for element in testing_list[1:]:
    if element < minimal:
        minimal = element

print(minimal)

# 2. Find minimal element of list using `built-in` function.
  
minimal = min(testing_list)
print(minimal)

testing_tuple = (2, 3, 'world', [1, 2, 3], 8)

# 3. Replace third element (`world`) with sorted string of these letters.

# Workaround as tuple is immutable.
testing_tuple = list(testing_tuple)
try:
    testing_tuple[2] = ''.join(sorted(testing_tuple[2]))
except IndexError:
    print('There is no third item in tuple.')
except TypeError:
    print('"%s" object is not iterable.' % testing_tuple[2])
testing_tuple = tuple(testing_tuple)
print(testing_tuple)
# 4. Catch possible errors for previous tasks.

# Implemented in 3rd task.
