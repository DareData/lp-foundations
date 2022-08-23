# Testing

## How to write unit tests for existing Python code

![Using tests to refactor a codebase](../images/b0bf092008be10cffa9b30080256114a74fcfc6615880045ab77892cb66d7b81.png)  

- Part 1 - [Link to YouTube video](https://youtu.be/ULxMQ57engo)
- Part 2 - [Link to YouTube video](https://youtu.be/NI5IGAim8XU)

This 45min video covers a practical example of adding unit tests to existing code, followed by a refactoring of the code. It's a great example of how to use tests to refactor code. You will get a sense on how refactoring can simplify test while improving the design.

After this lesson you should:

- Learn the criteria to use when selecting what piece of code to test first,
- Learn how to use the `pytest` framework,
- Know about `mock` objects, and how to use `pytest-monkeypatch`,
- See an example of dependency injection to make code more testable.

> **Note**: The author shows a `coverage` report. The package `pytest-cov` is a `pytest` plugin that generates coverage reports by adding the option `--cov` to your testing command.

## Testing DataFrames

[Link to Testing DataFrames tutorial](https://docs.google.com/document/u/1/d/11kl09lv2I47w1i70kwBbRMBzhprw5ja2VOm6gbzyzdc)

Testing data is a little bit different than testing regular Python code. In this lesson, you will learn how to test Pandas and Pyspark DataFrames.

After this lesson you should:

- Know how to test Pandas DataFrames with the `pandas.testing` module,
- Know how to test Pyspark DataFrames with local spark sessions.
