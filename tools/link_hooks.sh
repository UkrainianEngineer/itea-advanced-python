#!/bin/bash

set -e
set -o pipefail

repo_root=`git rev-parse --show-toplevel`

exit_code=0
current_dir=`pwd`

for file in `ls hooks`; do
 if [ -e "$repo_root/.git/hooks/$file" ]; then
     echo "Removing file: $file"
     rm -r "$repo_root"/.git/hooks/"$file"
 fi
 if [ -L "$repo_root/.git/hooks/$file" ]; then
     echo "Removing link: $file"
     rm -r "$repo_root"/.git/hooks/"$file"
 fi
 ln -s $current_dir/hooks/$file "$repo_root"/.git/hooks/"$file"
 current_exit_code=$?
 if [ $current_exit_code -ne 0 ]; then
   exit_code=$current_exit_code
 fi
done

if [ $exit_code -ne 0 ]; then
 text="Failed to commit. Please correct reported problems and retry."
 echo
fi
exit $exit_code
