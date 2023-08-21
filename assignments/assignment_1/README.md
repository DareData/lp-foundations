# Assignment 1: EU Life Expectancy

> **Warning**
> Before starting this assignment, make sure you have read the [project's setup instructions](../README.md) and have finished the [`pyproject` installation](../assignment_0/README.md).

There are 2 parts to this assignment: cleaning the data and ensuring good code quality. Remember to develop the assignments inside the `life_expectancy` folder.

Let's break it down:

```bash
assignments
├── life_expectancy    # This directory contains the package you'll be creating on the assignment
| ├── data             # Data files are to be kept in this directory
| └── tests            # Directory for tests. `pytest`, our testing framework, will try to find this folder and run all 
|                      #   tests inside it.
└── pyproject.toml     # Meta-information about the project
```

The datafiles are in TSV format in wide format. The first column is a composed one, containing 4 different information (unit, sex, age, geo). The next columns are temporal values, the life expectancy in years.

These are the code requirements for part one:

## Data cleaning

1. Create a script called `cleaning.py`.
2. This script should have a function called `clean_data` that does the following:
    1. Loads the `eu_life_expectancy_raw.tsv` data from the `data` folder.
    2. Unpivots the date to long format, so that we have the following columns: `unit`, `sex`, `age`, `region`, `year`, `value`.
    3. Ensures `year` is an `int` (with the appropriate data cleaning if required)
    4. Ensures `value` is a `float` (with the appropriate data cleaning if required, and do remove the `NaN`s).
    5. Filters only the data where `region` equal to `PT` (Portugal).
    6. Save the resulting data frame to the `data` folder as `pt_life_expectancy.csv`. Ensure that no numerical index is saved.
3. Verify that your code runs by running `pytest life_expectancy --cov`[^1].

If everything runs, congrats! Move on to the next part.

## Refactoring

For this refactoring section, we have 3 activities:

1. Run `pylint` on your code with `pylint life_expectancy.cleaning`. Some of the suggestions will make sense, others won't. For those that don't, add a pylint configuration to ignore them. Fix the ones that make sense. You should get a score of 10/10.
2. Ensure the call to `clean_data` is done inside a `if __name__ == "__main__":  # pragma: no cover` block. You can read more about the "pragma: no cover" [here](https://coverage.readthedocs.io/en/latest/excluding.html).
3. Include command-line options. We want the country to be a command-line option that you will then pass to the `clean_data` functions as an argument. The default should be `PT`. You can use either the `argparse` module or a third-party package for this, but remember to include it in the `pyproject.toml` file if it's the latter.
4. Update the tests in `tests/test_cleaning` to reflect the changes: namely, pass the `"PT"` as an argument to the `clean_data` function on line 10. After this, running `pytest life_expectancy --cov` should still work.

## Continuous integration

Now, let's create a CI pipeline for this project. We will use GitHub Actions for this.

1. Create a new personal and public repo for this project on GitHub.
   1. Ensure your code follows the structure described above. It can have other files, but it should have the `life_expectancy` folder (and your code in ), the `README.md` and `pyproject.toml` on the project root.
   2. It should have a `.gitignore` file. You can read more information on what it is [here](https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/) and [here](https://github.com/github/gitignore/blob/main/Python.gitignore) is a good example to use for python projects.
   3. Push your code to GitHub.
2. Create a new branch called `ci`. The pipeline should:
   1. Run `pytest` on the code
   2. Run `pylint` on the code.
   3. Be triggered on every push to the `main` branch and every pull request update.
3. Create a pull request from `ci` to `main`. Don't merge it yet! If the workflow triggers were correct, GitHub should try to run the workflow. If it doesn't or if it fails, try to fix it with additional commits to the `ci` branch.
4. Add a badge to the `README.md` file that shows the status of the pipeline. You can find the badge in the `Actions` tab of the repo. Select the workflow run and then click the "..." button: a "Create status badge" option should appear. Open the `ci` branch on your local machine (a quick way to do this, if you haven't created a local `ci` branch yet, is to use the `git switch ci` command), paste the provided markdown to the project's `README.md` and push this commit.
5. Merge the pull request when the pipeline succeeds.

[^1]: Do you want to know what the `--cov` flag does? It's a flag for the `pytest` command that tells it to run the code coverage tool. You can read more about it [on 06_testing/coverage.md](../../06_testing/coverage.md).
