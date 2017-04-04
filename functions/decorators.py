"""This module describes hot wo implement permission checker decorator."""

# Write custom function which returns your name or username.
# Write decorator which allows access for your user
# and prints `Permission denied` for other users.

# As a result you should create:
# 1) `get_user_info` function #returns your name or username.
# 2) decorator # raises Exception if `get_user_info` returns
#    not your  name or username.
# 3) `check_perms` function decorated by decorator.
#     returns `Allowed access` if validation was successful.

def get_user():
    return 'pivanchy'

def wrapper(fn):
    def wrapped(*args, **kwargs):
        if get_user() != 'pivanchy':
            raise Exception("Permission denied.")
        return fn(*args, **kwargs)
    return wrapped

@wrapper
def check_perms():
    print "Allowed access"

check_perms()
