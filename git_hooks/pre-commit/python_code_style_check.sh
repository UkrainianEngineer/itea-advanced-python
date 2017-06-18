#!/bin/bash

echo "Running 'python code style checker'..."

fail () {
    echo "$@: [FAILED]"
    exit 1
}


echo "checking pep8 conformance"
pep8 . || fail pep8
echo "Finished 'python code style checker' execution."
