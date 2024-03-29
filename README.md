<img src="/app/static/logo-with-name.png" height=180 />

PubMed Connections is a web application that facilitates
the analysis of the relationships between authors in the
PubMed database.

## Config

The [config.py](config.py) file is used to hold user
specific settings for the project. This includes
secret keys or email addresses. These values should
not be committed to the GitHub repository, but by
default git will want to include them in commits.
The following command can be used to keep
config.py from your commits,

```shell
git update-index --skip-worktree config.py
```

However, sometimes you may wish to push changes
that include changes within config.py. In these
cases, you should first manually remove all private
information from [config.py](config.py). After you
have done this, you can use the following command
to allow config.py to be included in commits,

```shell
git update-index --no-skip-worktree config.py
```

Once you have committed the changes to config.py,
you can mark the file as skip-worktree again, and
add your private information back.


## Conda Environment

This project uses a conda environment to manage its
dependencies. Instructions to install conda can be
found in the
[conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

**1. Creating the environment**

This only has to be done once. This command will
create a new conda environment that can be used
to run the website locally.
```shell
conda env create -f environment.yml
```

**2. Activating the environment**

This will activate the environment so that you
can run the website with all its dependencies
loaded.
```shell
conda activate pubmed-connections
```

**3. Updating the environment**

This will update the environment to include any
new dependencies that were added to the
`environment.yml` file.
```shell
conda env update --name pubmed-connections --file environment.yml --prune
```
