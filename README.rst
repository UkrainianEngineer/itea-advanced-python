https://travis-ci.org/pivancy/itea-advanced-python.svg?branch=master
=======
.. image:: https://travis-ci.org/pivancy/itea-advanced-python.svg?branch=master
    :target: https://travis-ci.org/pivancy/itea-advanced-python

What is this repository about
=============================

This repository created as a tooltip for my students from ITEA.
Some homeworks are described here!

Installation
============

1. Activate virtual environment:
    `source <virtual_env>/bit/activate`

2. Install required packages:
    `pip install -r requirements.txt`

3. Copy git hook into your local repository:
    `cp git_hooks/* <repository_directory>/.git/hooks/`


Code style checks
=================

PEP8 code style checker added into git `pre-commit` hook.
It executes on each commit and fails before commit if some issues exist.
Code style may be checked using `pep8` tool:
    `pep8 <folder_with_python_modules>`
or
    `pep8 <python_module>`


Unittests execution
===================

All existing unittests are running before each commit.
Commit fails if some tests fails. All tests are running using `nosetests` tool.
Status of unittests may be verified using:
    `nosetests`
or
    `nosetests <python_module_with_unittests>`

Installation guideline
======================

 - Activate your virtual environment: `source <virtual_env>/bin/activate`
 - Install needed packages: `pip install -r requirements.txt`
 - Run Django server: `python manage.py runserver 0.0.0.0:8000`


Deployment automatically
========================

After each commit into `master` branch application automatically deploys
into AWS EC2 instance.

Auto-deployment may be done using link:
http://crypt.codemancers.com/posts/2016-12-26-autodeploy-from-github-using-aws-codedeploy/

:TODO: pivanchy: Configure web server(Apache, nginx, etc. ) instead of Django server.
