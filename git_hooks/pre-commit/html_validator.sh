#!/bin/bash

echo "Running 'html validator'..."

repo_root=`git rev-parse --show-toplevel`

fail () {
    echo "$@: [FAILED]"
    exit 1
}

if [ -d "$repo_root/cover" ]; then
  rm -rf $repo_root/cover/
fi

html_files=`find $repo_root -type f -name '*.html'`

for file in $html_files; do
  html_lint.py --printfilename $file || fail html_lint.py
done

echo "Finished 'html validator' execution."
