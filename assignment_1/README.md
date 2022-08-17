# Assignment 1: EU Life Expectancy

There are 2 parts to this assignment: cleaning the data and ensuring good code quality.

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
3.  Verify that your code runs by running `pytest assignment_1 --cov`.

If everything runs, congrats! Move on to the next part.

## Refactoring

For this refactoring section, we have 3 activities:

1. Run `pylint` on your code with `pylint assignment_1/cleaning`. Some of the suggestions will make sense, others won't. For those that don't, add a pylint configuration to ignore them. Fix the ones that make sense. You should get a score of 10/10. 
2. Create an entry point for the script.

```python
if __name__ == "__main__":  # pragma: no cover
    clean_data()
```
2. Include command-line options. We want the country to be a command-line option. The default should be `PT`. You can use either the `argparse` module or a third-party package for this, but remember to include it in the `pyproject.toml` file if it's the latter.
3. Update the tests in `tests/test_cleaning` to reflect the changes. Runnings `pytest assignment_1 --cov` should still work.
4.  Include a GitHub Action to run the tests and linting.
