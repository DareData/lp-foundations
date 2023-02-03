# Assignment 3: Testing

Assignment 3 is about testing.

We currently have a single integration test, but that test is very dangerous: it deletes any files created by the application - including ones resulting from its normal usage. Ideally, we would either not have our tests change actual data and not depend on connectivity in order to work, or have a database made specifically for testing.

> Don't forget to create a branch for this assignment.

## 1- Fixtures

1. Create a fixture based on the `life_expectancy\data\eu_life_expectancy_raw.tsv` data. It can be a sample, so that our tests run faster. Then, replace the `life_expectancy\tests\fixtures\pt_life_expectancy_expected.csv` with the new expected data.
2. Modify your `main` function so that the cleaned DataFrame is always returned. That will allow you to compare it with the expected fixture.
3. Make the tests consume this fixture instead of the actual data. The idea of using fixtures instead of collecting data from a database will ensure our code is not dependent on connectivity. This will make our lives easier when we want to run our tests in a CI/CD pipeline.

## 2- Unit tests and Mocks

1. Right now you should have more python modules. If not, ensure you have at least 2: one for data cleaning and one for loading/saving data.
2. We also have a single integration test, but we should have one unit tests for each of the non-private functions[^1] we have. So, for example, if you have 3 public functions, you should have 3 unit tests.
   1. On the units above, ensure that any test to functions that save data uses a mock
   2. You can do this by patching the `pd.DataFrame.to_csv` method to make the tests not write to a file. Instead, it should just print out a message.
   3. Then, assert that the `pd.DataFrame.to_csv` method is being called. As a bonus, by setting up your tests in this fashion, we can ensure no data transformations modifies any actual data.

[^1]: Yes, you can also test internal functions if you want to (specially for training purposes). But in the real world, remember that you really believe a particular internal function should be tested, that's a strong indicator it should be decoupled and placed inside its own module - thus making it public.

## 3- VSCode Test Discovery

If you're on VSCode, you can use the [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) extension to run your tests. It will automatically discover your tests and you can run them from the Test Explorer tab.

1. Run your test suite using the Test Explorer. You should see the integration test and the unit test.

## 4- Code Review

As with the previous assignment, a peer should review your code and you will be reviewing the code of a fellow colleague.
