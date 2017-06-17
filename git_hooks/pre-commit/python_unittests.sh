#!/bin/bash

echo "Running 'python unittests'..."

do_nosetests() {
    $1 -v --with-coverage --cover-html
}

fail () {
    echo "$@: [FAILED]"
    exit 1
}

echo "checking unit test suite (py2)"
do_nosetests nosetests || fail nosetests

# Remove useless *.pyc files.
repo_root=`git rev-parse --show-toplevel`
find $repo_root -name \*.pyc -delete

echo "Finished 'python unittests' execution."
