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

echo "Finished 'python unittests' execution."
