# Assignment 3: Testing

Assignment 3 is about testing.

We currently have a single integration test and this test was very dangerous: before you refactored the clean_data() function, it would overwrite any files created by the application - including ones resulting from its normal usage. Ideally, we would either not have our tests change actual data and not depend on connectivity in order to work, or have a database made specifically for testing. Therefore, let us solve this issue in this exercise.

> Don't forget to create a branch for this assignment.

## 0- VSCode Test Discovery

In order to make your life easier during this assignment, we want to give you a little tip. If you're on VSCode, you can use the [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) extension to run your tests. It will automatically discover your tests and you can run them from the Test Explorer tab. At this point, if you have refactored your functions as requested in [assignment_2](../assignment_2/README.md) your tests should be failing.

## 1- Fixtures

0. If you recall the structure from [assignment_0](../assignment_0/README.md), we currently have two fixtures, one for the expected output of the portuguese life expectancy dataframe and another one for the european life expectancy dataframe.
1. Following best practises, we want to create a fixture that represents our data. The idea of using fixtures instead of collecting data from a database will ensure our code is not dependent on connectivity. This will make our lives easier when we want to run our tests in a CI/CD pipeline. Start from the current data in `life_expectancy\data\eu_life_expectancy_raw.tsv` and create a fixture `life_expectancy\tests\fixtures\eu_life_expectancy_raw.tsv` for the tests to consume. Since we only want to test our functions, this fixture does not need to be a copy of the original, but could rather be a smaller sample, so that our tests run faster.
2. Now that we have _our_ sample, we need a fixture of the expected output associated to it. You can use your existing `life_expectancy` module to generate a `pt_life_expectancy_expected.csv` file that will replace the current file at `life_expectancy\tests\fixtures\pt_life_expectancy_expected.csv`. Finally, include the necessary code to import this new fixture in the `conftest.py` file.
3. Modify your `main` function so that the cleaned DataFrame is always returned. That will allow you to compare it with the expected fixture.
4. Modify the current test in `test_cleaning.py` to consume these two fixtures instead of the actual data.
> Don't forget to pass the new fixture an argument of the test functions!  

## 2- Unit tests and Mocks

0. Right now you should have more python modules. If not, ensure you have at least 2: one for data cleaning and one for loading/saving data. 
```bash
.
├── LICENSE.md
├── README.md
├── life_expectancy  # This directory contains the package you'll be creating
│   ├── __init__.py  # This file is required for Python to recognize this directory as a module
│   ├── data         # Data files are to be kept in this directory
│   │   └── eu_life_expectancy_raw.tsv
│   ├── temp.py      # A temporary file to test the installation. You will delete it later.
│   │── tests        # Directory for tests.
│   │   ├── __init__.py
│   │   ├── conftest.py  # `conftest.py` is a special pytest file. It contains fixtures and plugins.
│   │   ├── fixtures     # Fixtures are reusable objects that can be used in tests.
│   │   │   ├── eu_life_expectancy_expected.csv
│   │   │   └── pt_life_expectancy_expected.csv
│   │   ├── test_cleaning.py  # Tests for the cleaning module (assignment 1)
│   │   └── test_pyproject.py  # Tests for the pyproject installation (this assignment)
|   ├── cleaning
|   |   ├── __init__.py
|   |   ├── cleaning.py
|   ├── load_save_data
|   |   ├── __init__.py
|   |   ├── load_data.py
|   |   ├── save_data.py  
|
└── pyproject.toml
```
1. We also have a single integration test, but we should have one unit tests for each of the non-private functions[^1] we have. So, for example, if you have 3 public functions, you should have 3 unit tests.
   1. On the units above, ensure that any test to functions that save data uses a mock
   2. You can do this by patching the `pd.DataFrame.to_csv` method to make the tests not write to a file. Instead, it should just print out a message.
   3. Then, assert that the `pd.DataFrame.to_csv` method is being called. As a bonus, by setting up your tests in this fashion, we can ensure no data transformations modifies any actual data.

[^1]: Yes, you can also test internal functions if you want to (specially for training purposes). But in the real world, remember that you really believe a particular internal function should be tested, that's a strong indicator it should be decoupled and placed inside its own module - thus making it public.


## 4- Code Review

As with the previous assignment, a peer should review your code and you will be reviewing the code of a fellow colleague.
