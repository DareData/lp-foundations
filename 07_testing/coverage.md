# Test Coverage

Test coverage is a software development metric that measures how much of your code is covered by tests. It's typically expressed as a percentage, where higher percentages indicate more extensive testing.

Test coverage is important for several reasons:

* It helps identify untested parts of the code, which could contain potential bugs or vulnerabilities.
* It serves as a quality indicator, as higher coverage usually leads to more robust and reliable software.
* It facilitates decision-making regarding further testing, as developers can focus their efforts on areas with lower coverage.

`pytest` is a very popular testing framework for Python, and it's what we will be using in our assignments. We will also be using the `pytest-cov` plugin to measure test coverage. For your assignments, everything is already defined in the `pyproject.toml` file, so you don't need to install anything extra after installing the local package.

If you want to install `pytest` and `pytest-cov` manually, follow these steps:

```shell
pip install pytest pytest-cov
```

Then run `pytest` with the `--cov` flag:

```shell
pytest tests/ --cov
```

> **Note**: Remember that a high coverage doesn't guarantee bug-free code, as it only shows which parts of the code are executed during testing, not if the tests are effective or meaningful. Don't write unnecessary tests just to increase coverage.

## HTML Reports

Sometimes you want to see exactly what lines are not being covered by tests. To answer that question, you can generate an HTML report.

### Using `pytest-cov` plugin

Run `pytest` with the `--cov` flag, specifying the source directory and the desired output format (in this case, 'html'):

```shell
pytest --cov=my_project --cov-report html tests/
```

Note that now we must specify the coverage source directory, which is the directory containing the Python files that we want to measure coverage for. In this case, it's the `my_project/` directory.

This command will generate an HTML report in the `htmlcov/` directory by default.

Open the `index.html` file in the `htmlcov/` directory using a web browser. This will display the test coverage report, including the percentage of coverage for each file, and the lines that are covered or missed by the tests.
