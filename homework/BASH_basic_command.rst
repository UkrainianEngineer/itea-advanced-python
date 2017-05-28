Introduction
============

This file contains basic tasks for those, who want to improve their skills in
Linux command line.

Tasks
~~~~~

1. Find all `*.pyc` files in project using single command in command line.
    **$ find . -name *.pyc**

  1.1. Delete all `*.pyc` files from project using single command in command line.
    **$ find . -name *.pyc -delete**

2. Calculate number of files in directory using command line.
    **$ ls -A | wc -l**

3. Calculate number of `*.py` files in project.
    **$ find . -type f -name *.py | wc**

4. Print list of files in some directory sorted by time modified.
    **$ ls -alS**

5. Open file for real time reading.
    **$ cat -n myfile.txt**

6. Print first 5 lines of file.
    **$ head -n5 myfile.txt**

7. Print last 5 lines of file.
    **$ tail -n5 myfile.txt**

8. Open huge file for reading from command line.
    (vi, vim, nano, gedit, etc. are not applicable, they will opens too long.)