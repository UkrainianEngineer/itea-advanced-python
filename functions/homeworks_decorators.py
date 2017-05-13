"""This module describes homework related to decorators.

   Author: pivanchy.
"""

# Implement `retry` decorator.
# If some part of code in decorated function fails, try to re-run it again.
# If decorated function executes successfully, you don't need to re-run it.
#
# 1) add some global variable like `RETRIES = 4`.
#    Use this variable for your retry decorator.
#    Failed function should retries up to 4 times.
#
# Example:
#   RETRIES = 4
#   def decorator(...):
#       # Use `RETRIES` variable here somehow.
#
#   @decorator
#   def my_func():
#       # Doing something.
#
# 2) Improve previous task to make it possible to pass a parameter
#    into your decorator.
#
# Example:
#   def decorator(...):
#       # Implement decorator here.
#
#   @decorator(retries=4)
#   def my_func():
#       # Doing something.
#
#  3) Implement decorator which caches data.
#     It mean that for first run of function it should print something like:
#         `Calculated value. => <calculated_value>`
#     For second, third, ... runs it should print:
#         `Using data from cache. => <value_from_cache>`
#
#  Example:
#
# @cached
# def my_func():
#     # Doing something.
#     # E.g.:
#     return 'Hello, world!"
#
#  my_func() # prints `Calculated value. => Hello, world!`
#  my_func() # prints `Using data from cache. => Hello, world!`
#  my_func() # prints `Using data from cache. => Hello, world!`
#  my_func() # prints `Using data from cache. => Hello, world!`
