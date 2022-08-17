# Assignment 1: EU Life Expectancy

There are 2 parts to this assignment: cleaning the data and ensuring good code quality. The project is in the `life_expectancy` folder.

The datafiles are in TSV format in wide format. The first column is a composed one, containing 5 different information (unit, sex, age, geo). The next columns are temporal values, the life expectancy in years.

These are the code requirements for part one:

## Data cleaning

1.  Create a script called `cleaning.py`.
2.  This script should have a function called `clean_data` that does the following:
    1.  Loads the `eu_life_expectancy_raw.tsv` data from the `data` folder.
    2.  Unpivots the date to long format, so that we have the following columns: `unit`, `sex`, `age`, `region`, `year`, `value`.
    3.  Ensures `year` is an `int` (with the appropriate data cleaning if required)
    4.  Ensures `value` is a `float` (with the appropriate data cleaning if required)
    5.  Filters only the data where `region` equal to `PT` (Portugal).
    6.  Save the resulting data frame to the `data` folder as `pt_life_expectancy.csv`. Ensure that no numerical index is saved.	
3.  Verify that your code runs by running `pytest life_expectancy --cov`.

If everything runs, congrats! Move on to the next part.

## Refactoring

For this refactoring section, we have 3 activities:

1. Run `pylint` on your code with `pylint life_expectancy/cleaning`. Some of the suggestions will make sense, others won't. For those that don't, add a pylint configuration to ignore them. Fix the ones that make sense. You should get a score of 10/10. 
2. Create an entry point for the script.

```python
if __name__ == "__main__":  # pragma: no cover
    clean_data()
```
2. Include command-line options. We want the country to be a command-line option. The default should be `PT`. You can use either the `argparse` module or a third-party package for this, but remember to include it in the `pyproject.toml` file if it's the latter.
3. Update the tests in `tests/test_cleaning` to reflect the changes. Runnings `pytest life_expectancy --cov` should still work.

## Continuous integration

Now, let's create a CI pipeline for this project. We will use GitHub Actions for this. 

1. Create a new repo for this project.
2. Create a new branch called `ci`. The pipeline should:
   1. Run `pytest` on the code
   2. Run `pylint` on the code.
   3. Be triggered on every push to the `main` branch and every pull request update.
3. Create a pull request from `ci` to `main`. Don't merge it yet! 
4. Add a badge to the `README.md` file that shows the status of the pipeline. You can find the badge in the `Actions` tab of the repo. Push this commit.
5. Merge the pull request when the pipeline succeeds.
