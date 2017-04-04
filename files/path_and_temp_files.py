"""This module describes how to use system paths and temporary files.

   Author: pivanchy.
"""

import os
import tempfile

# Print current directory.
pwd = os.getcwd()
print pwd

# Print absolute path to current directory.
print os.path.abspath(pwd)

# Print base name of current directory.
print os.path.basename(pwd)

# Print list of properties and methods.
print dir(os.path)


# Use temporary file
with tempfile.NamedTemporaryFile() as fin:
    fin.write('Some text goes here')
    fin.flush()
    with open(fin.name, 'r') as fout:
        data = fout.readlines()
        print "Data from temporary file: %s" % data
