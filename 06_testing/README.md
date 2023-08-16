# Testing

## Introduction to Unit Testing with PyTest

![Unit Testing with PyTest](./../images/unit-test-with-pytest-cover.png)

This video is meant to be your first contact with Pytest. It will show you how to write unit tests for a simple shopping cart application..

- Unit tests are functions that check if your code or application works as intended.
- If the application works correctly, tests should pass. If there's a bug or improper implementation, tests should fail.
- Unit tests allows you to quickly detect problem when you are making changes to existing code. This is especially important when working in a team.
- Refactoring without unit tests can be risky.
- Unit tests ensure new functionality doesn't break existing code.

After this lesson you should know:

- The basics of Pytest: Understand the importance of unit tests, how to set up PyTest, and the conventions for writing and naming tests.
- How to write and run specific tests, including checking for exceptions.
- Some best practices: Like making sure tests fail for the right reasons, and get introduced to the concept of reducing duplicate code in tests with fixtures.

## More on Mock objects

In the last video you were introduced by the concept of mock objects, where the author replaced a parameter with a mock object. However, that's not something we usually do. This is because we don't have access to the thing we want to mock most of the times.

For example, in your homework, you will have to test a function that uses pandas' `read_csv` function. The `read_csv` method is inside the function: you can't access it directly to replace it with a mock object. That's why you need to use the `patch` decorator.

A couple of warnings about the next video:

1. It uses the `python.unittest` framework instead of `pytest`. The concepts are the same, but the syntax is a little different. However, the important thing is that the way you use patches and mocks also work for pytest.
2. From the 3:30 to the 4:15 mark, the author talks about the "setups" and "teardowns. This is the only part that's specific to `unittest`. You can skip it.

![mock patch in seven minutes](./../images/mock-path-seven-minutes.png)

## Testing DataFrames (0:10)

[Link to Testing DataFrames tutorial](testing_dataframes.md)

Testing data is a little bit different than testing regular Python code. In this lesson, you will learn how to test Pandas and Pyspark DataFrames.

After this lesson you should:

- Know how to test Pandas DataFrames with the `pandas.testing` module,
- Know how to test Pyspark DataFrames with local spark sessions.

## What should you test?

Potentially one can test _everything_. However, this is not practical - nor desirable. The goal of testing is to ensure that the code is working as expected. This means that you should test the code that is critical to the application. For example, if you are building a web application, you should test the code that handles the HTTP requests. If you are building a data pipeline, you should test the code that handles the data transformations.

There are 2 things you should always have:

1. You should have an integration test that runs the entire application. This is to ensure that the application is working as expected when all the pieces are put together. This is also called an end-to-end test.
2. You should have at least one unit test for each _public_ function. This is because public functions are the one that will be imported and used by other applications or modules.

What about the private functions? Those function that start with a `_` or a `__`? You don't really need to test those. The other problem with testing internal functions is that it increases the likelihood of your tests failing for the wrong reasons. For example, when changing something internal, that doesn't break anything but forces you to spend a long time updating all tests.

But what if the internal function is critical to the application? If you really believe a particular internal function should be tested, that's a strong indicator it should be decoupled. Move it to a module of its own and make that function public.

## Extra resources

These are optional, but hey can be useful if you want to learn more about testing.

- [Code coverage](coverage.md) - What is code coverage and how to use it with `pytest`.
