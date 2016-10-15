# Using git for the greater good

Other good references:

A [simple guide.](http://rogerdudler.github.io/git-guide/)

Read the [docs.](https://git-scm.com/)

## What not to do

```
legacy_code/
    old_versions/
	    oldercode.py
		evenoldercode.py
		nounderscoreshere.py
		nocommentshere.py
    my_code_actual_final.py
    my_code_final.py
    my_code_new.py
	my_code.py
    my_code_refactor.py
    my_code_v2.py
    my_code_v3.2.py
    my_code_v3.py
    my_code_v4.py
```

## What is distributed version control?

* Local version control: can I recover from making a silly mistake?

* Centralized version control: can I recover from my computer catching on fire?

* Distributed version control:  can I work on my code with someone else simultaneously editing the same code?

From the docs

![git-scm](https://git-scm.com/book/en/v2/book/01-introduction/images/snapshots.png)

![git-scm](https://git-scm.com/book/en/v2/book/01-introduction/images/distributed.png)

From Randall Monroe

![xkcd wisdom](https://imgs.xkcd.com/comics/git.png)


## A simple workflow

Let's go through a quick setup of an example repository.

### Git init

The easiest way is to make a new repository on GitHub or BitBucket. Then this repo can be cloned (copied) to your local machine with

```
git clone git@github.com:ucsc-astro/myrepo.git
```

Note that this will make a new folder in the current directory.

Alternatively, you can make a new repository locally, then (optionally) synch it with a remote repository

```
mkdir myrepo
cd myrepo
git init
git remote add origin git@github.com:ucsc-astro/myrepo.git
git push --set-upstream origin master
```

### Make some changes

Let's make a file.

```
echo 'hello git!' > hello.txt
```

We want to add this file to the repository.

```
git add hello.txt
```

But this only adds changes to the staging area, not to the repository.

```
git commit
```

This will bring you to a text editor, where you can write a short description of the change, and save it.  To do this all on one line do

```
git commit -m  'first commit'
```

Now we have saved a commit (like a "save as" checkpoint). Let's put this change on the remote server.

```
git push origin master
```

And [there](https://github.com/ucsc-astro/myrepo) it is!

### What did we just do?

From the docs

![from git-scm](https://git-scm.com/book/en/v2/book/01-introduction/images/areas.png)

## The undo button

Things will go wrong. How do you deal with them?

### The oops zone

How to fix minor mistakes

* `git commit --amend` will add any changes to the staging area to the previous commit

* `git reset HEAD target_file` will remove `target_file` from the staging area. `HEAD` is a reference to the most recent commit. This command can get confusing fast.  See the [docs](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)

```
git revert 0766c053..HEAD
git commit
```
will revert the tree to the git hash `0766c053`, and commits that old one to the tree. To figure out which hash corresponds to which commit, use `git log`.

### The danger zone

How to deal with less minor mistakes (at the risk of losing data).  Note that, barring all copies of a repository being deleted, *any changes which have been committed can be recovered*.

* `git checkout -- target_file` will replace `target_file` in the working directory with the version from the previous commit.

## Branching off

Let's say we want to work on something new and dangerous without having to worry about doing any of the undo nonsense above. To do this, we can branch off from the master branch.

```
git branch my_new_feature
git checkout my_new_feature
```
Or in one line, `git checkout -b my_new_feature`. The `git branch` command makes a new branch pointing to the current commit. The `git checkout` command points our current commit to that branch, and changes the working directory to match that new branch.  Since the new branch is currently the same as the old one, we don't see the working directory change at all.

Let's now make some bad changes and commit them.
```
echo "breaking change" > mission_critical_code.py
git rm necessary_information.txt
git add mission_critical_code.py
git commit -m "hope this works"
```
When we notice that everything in this new feature branch is on fire, we can just switch back to the old, working master branch as such:
```
git checkout master
```
Again, note that performing a checkout will change your working directory to match the named commit, so if there are any changes in the working directory which are not committed, you need to either revert them or stash them (e.g., with `git stash`). This latter option allows for a recovery if you realize you accidently checked out over something you wanted to keep.

I highly encourage you to read the [docs](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) for a much nicer visual explanation of branches.

## Working nicely with others

A nice review of workflows from [Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows).

## Useful things

* `git status` - check what files are modified or staged for commit

* `git diff` - see any file differences between commits

* `git log` - see the revision history

* `git fetch` - get information from the remote repository

* `git remote` - manage remote repository list

* `git rm` - removes files from the repository

* any files listed in a `.gitignore` file will be ignored

## Other considerations

Save your name and email with

```
git config --global user.name "Your Name"
git config --global user.email youremail@ucsc.edu
```

You can change your text editor for commits (default is vim) with

```
git config --global core.editor emacs
```

To avoid logging in everytime you connect to a remote repo, upload your ssh public key to GitHub or BitBucket. See [here](https://help.github.com/articles/generating-an-ssh-key/) for details.

## A git glossary

See also on [GitHub](https://help.github.com/articles/github-glossary/)

* branch - a named reference to a particular commit

* clone - to make a copy of the repository

* commit - to save the changes made in the staging area to the repository

* diff - to check how a file is different between commits

* fetch - to get information from a remote repository

* fork - to copy a remote repository to a new remote repository

* hash - a mapping of anything to a unique-ish 40 character string, used by git to have unique references to each commit

* HEAD - a reference to the current commit, that is, the commit to which the next commit will reference back

* master - conventionally, the primary branch of a repository

* merge - to bring in changes from one branch to another

* modified - describes file changes that aren't yet tracked in the staging area

* origin - a conventional name for the default remote repository

* pull - to read new changes from a remote repository into the local repository

* pull request - to ask for changes to be made from the local repository to the remote master branch

* push - to write changes from the local repository to a remote repository

* remote - a server with a git repository

* repository - a directory tree with a revision history

* upstream - a conventional name for the remote repository of which the local one is a fork

