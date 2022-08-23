# Assignment 3: Testing

Assignment 3 is about testing. We currently have a single integration test, but that test is very dangerous: it deletes any resulting files - including the one the normal usage of module would create. Ideally, we would either not have our tests change actual data and not depend on connectivity in order to work, or have a database made specifically for testing.

> Don't forget to create a branch for this assignment.

## 1- Fixtures and Mocks

1. Create a fixture based on the `life_expectancy\data\eu_life_expectancy_raw.tsv` data. It can be a sample, so that our tests are faster, but then replace the `life_expectancy\tests\fixtures\pt_life_expectancy_expected.csv` with the new expected data. Make the tests consume this fixture instead of the actual data. This way, assuming a scenario where the data comes from a database, we don't need access to it in order to run the tests.
2. Patch the `pd.DataFrame.to_csv` method to make the integration test not write to a file. Instead, it should just print a message. Then, assert that the method is being called with the correct arguments. Modify your function so that the modified is always returned and that you can compare it with the expected fixture. This way, we can still test the data transformations without having to worry about the tests changing the actual data.

## 2- VSCode Test Discovery

If you're on VSCode, you can use the [Python Test Explorer](https://marketplace.visualstudio.com/items?itemName=LittleFoxTeam.vscode-python-test-adapter) extension to run your tests. It will automatically discover your tests and you can run them from the Test Explorer tab.

## 3- Unit tests

1. Right now you should have more python modules. If not, ensure you have at least 2: one for data cleaning and one for loading/saving data.
2. We also have a single integration test, but we should have unit tests for each of the non-private functions we have.

## 4- Code Review

As with the previous assignment, a peer should review your code and you will be reviewing the code of a fellow colleague.
