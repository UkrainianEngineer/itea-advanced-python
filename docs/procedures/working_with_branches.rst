Introduction
~~~~~~~~~~~~

All branches should be up-to-date with `release` branch to have all
actual changes.

Feature branch synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each `feature` branch should be synchronized with `release` branch.
Before `feature` branch synchronization local `release` branch should be
synchronized with remote `release` branch.

Synchronize local `release` branch with remote:
    `git checkout release`
    `git pull`

Synchronize `feature` branch with `release` branch:
    `git checkout <name_of_feature_branch>
    `git merge release`

Last 2 commands merges changes from `release` into `<name_of_feature_branch>`.

Merging conflicts
~~~~~~~~~~~~~~~~~

If the same parts of files changed in two separate branches, merging conflicts
will appear during merging these branches.

Conclicts resolution
~~~~~~~~~~~~~~~~~~~~

For resolving merging conflicts author of commit should check changes from both
branches and create one file with important changes from both branches.
Aggregated file should be commited and merged.

Convert branch into tag
~~~~~~~~~~~~~~~~~~~~~~~

After merging `feature` branch into `release` branch, `feature` branch may be
not needed anymore. As we may need to restore changes from this branch for
some reason, it is better to convert this branch into tag before removing.

Convert branch into tag:
    `git checkout <name_of_branch_for_tagging>`
    `git tag -a <branch_name> -m <message>`
These commands creates a tag with name `<branch_name>` in current repository.
It may be restored in case of some specific reason.
After tagging branch it may be removed.

Remove remote branch:
    `git push origin --delete <branch_name>`

Remove local branch:
    `git branch -d <branch_name>`
