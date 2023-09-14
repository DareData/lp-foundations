# Assignment 3: Testing

Assignment 3 is about testing.

We currently have a single integration test. But it was a very dangerous test: before you refactored the clean_data() function, it would overwrite any files created by the application - including ones resulting from its normal usage. Ideally, we would either not have our tests change actual data and not depend on connectivity in order to work, or have a database made specifically for testing. Let us solve this issue in this exercise.

> Don't forget to create a branch for this assignment.

## 1- VSCode Test Discovery

In order to make your life easier during this assignment, we want to give you a little tip. If you're on VSCode, you can use the [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) extension to run your tests. It will automatically discover your tests and you can run them from the Test Explorer tab. At this point, if you have refactored your functions as requested in [assignment_2](../assignment_2/README.md) your tests should be failing.

## 2- Fixtures

0. If you recall the structure from [assignment_0](../assignment_0/README.md), we currently have two fixtures, one for the expected output of the portuguese life expectancy dataframe and another one for the expected european life expectancy dataframe (what is, without the PT filter).
1. We want to create a fixture that represents our input data. The idea of using fixtures instead of collecting data from a database will ensure our code is not dependent on connectivity. This will make our lives easier when we want to run our tests in a CI/CD pipeline. Here's how to create them:

   * **Input fixture**: Let's create our new input fixture by loading the `life_expectancy\data\eu_life_expectancy_raw.tsv`, creating a sample, and saving it as `life_expectancy\tests\fixtures\eu_life_expectancy_raw.tsv` [^1]. Remember that your sample must contain the elements you wish to test. For example, if you want to filter a given region, you fixture has to contain at least one row with that region.
   * **Expected fixture**: Now let's create the fixture for the expected result. Since you have changed `life_expectancy\tests\fixtures\eu_life_expectancy_raw.tsv` to be a sample, now your expected output _should_ be the corresponding image of this sample! Therefore, use your code on that input fixture data to generate the corresponding `life_expectancy\tests\fixtures\eu_life_expectancy_expected.csv` file.

2. Finally, include the necessary code to import these new fixtures in the `conftest.py` file.
3. Modify your `main` function so that the cleaned DataFrame is always returned. That will allow you to compare it with the expected fixture.
4. Modify the current test in `test_cleaning.py` to consume these two fixtures instead of the actual data.

   > Don't forget to pass the new fixture an argument of the test functions!  

5. Final touch: if you read the docstring of the `run_before_and_after_tests` function in the `life_expectancy\tests\conftest.py` file, you will see that by now, the function will be doing nothing... and, if it does nothing, it's dead code and dead code must be removed :smiling_imp:!

[^1]: The only reason why you can safely create this fixture is because we had that passing test on the 1st assignment. That's how you knew whether your code was doing what they it supposed to. In a real-world scenario without previous tests, you would first have to manually make sure that your procedures and functions are correct, otherwise you would create lying fixtures (i.e. fixtures that assume your code is correct when, in fact, it is not)!

## 3- Unit tests and Mocks

0. Right now you should have more python modules. If not, ensure you have at least 2: one for data cleaning and one for loading/saving data [^2].

   ```bash
   .
   ├── LICENSE.md
   ├── README.md
   ├── life_expectancy  # This directory contains the package you'll be creating
   │   ├── __init__.py  # This file is required for Python to recognize this directory as a module
   │   ├── data         # Data files are to be kept in this directory
   │   │   └── eu_life_expectancy_raw.tsv
   │   │── tests        # Directory for tests.
   │   │   ├── __init__.py
   │   │   ├── conftest.py  # `conftest.py` is a special pytest file. It contains fixtures and plugins.
   │   │   ├── fixtures     # Fixtures are reusable objects that can be used in tests.
   │   │   │   └── <the-fixtures-you-created>
   │   │   ├── test_cleaning.py  # Tests for the cleaning module (assignment 1)
   │   │   └── test_pyproject.py  # Tests for the pyproject installation (this assignment)
   |   ├── module_1.py  # Your modules
   |   ├── module_2.py  
   |   ├── ...
   |   └── module_n.py
   |
   └── pyproject.toml
   ```

1. We also have a single integration test, but we should have one unit tests for each of the non-private functions[^3] we have. So, for example, if you have 3 public functions, you should have 3 unit tests.
   1. On the units above, ensure that any test to functions that save data uses a mock
   2. You can do this by patching the `pd.DataFrame.to_csv` method to make the tests not write to a file. Instead, it should just print out a message.
   3. Then, assert that the `pd.DataFrame.to_csv` method is being called. As a bonus, by setting up your tests in this fashion, we can ensure no data transformations modifies any actual data.

[^2]: A module is just a python script (or a folder with a `__init__.py` file) that's meant to be imported instead of run directly.
[^3]: Yes, you can also test internal functions if you want to (specially for training purposes). But in the real world, remember that you really believe a particular internal function should be tested, that's a strong indicator it should be decoupled and placed inside its own module - thus making it public.

## 4- Code Review

As with the previous assignment, a peer should review your code and you will be reviewing the code of a fellow colleague.
