Introduction
~~~~~~~~~~~~

For better quality of code we use a lot of git **pre-commit** hooks.

Each hook should runs fine. If there is some issues, they should be reported.

Each team member may extend list of hooks, but can't remove some of them.
Each **pre-commit** hook executes before commit.

Python code style checker
~~~~~~~~~~~~~~~~~~~~~~~~~

This **pre-commit** hook verifies quality of Python code according
to PEP-8 recommendations.

It fails if some of rules were skipped by developer.
It validates all of existing Python files in the project.

Unittests executor
~~~~~~~~~~~~~~~~~~

This hook runs all of existing unittests. All of these tests should executes
without errors.

If there are some errors, author of commit should fix them.
Code coverage shouldn't decrease.

HTML linter
~~~~~~~~~~~

As it is not too easy to review HTML code, we use additional hook for
validation of HTML pages and templates.

It helps us to find critical things
before core review process. It validates all of existing HTML pages in project.

