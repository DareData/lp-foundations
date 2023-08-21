# Assignment 0: Project Setup

Before we dive into the assignments, we need to set up our project. Let's look at its structure first:

```bash
.
├── LICENSE.md
├── README.md
├── life_expectancy  # This directory contains the package you'll be creating
│   ├── __init__.py  # This file is required for Python to recognize this directory as a module
│   ├── data         # Data files are to be kept in this directory
│   │   └── eu_life_expectancy_raw.tsv
│   ├── temp.py      # A temporary file to test the installation. You will delete it later.
│   └── tests        # Directory for tests.
│       ├── __init__.py
│       ├── conftest.py  # `conftest.py` is a special pytest file. It contains fixtures and plugins.
│       ├── fixtures     # Fixtures are reusable objects that can be used in tests.
│       │   ├── eu_life_expectancy_expected.csv
│       │   └── pt_life_expectancy_expected.csv
│       ├── test_cleaning.py  # Tests for the cleaning module (assignment 1)
│       └── test_pyproject.py  # Tests for the pyproject installation (this assignment)
└── pyproject.toml
```

For this assignment, you need to package the project and install it in editable mode. Here's the caveat: the `pyproject.toml` file is already there, but it's incomplete! You need to fill in the missing fields.

## Instructions

1. Try running the `tests/test_pyproject.py` file first - it should **fail**. You can do it with:

    ```python
    pytest life_expectancy/tests/test_pyproject.py
    ```

    Depending on whether you already have `pytest` installed, the command might not even work. If that's the case, don't worry. It will be installed in the next steps.  

2. Complete the `pyproject.toml` file:
   1. The project name should be `life_expectancy`.
   2. The project version should be `0.1.0`.
   3. Don't forget to add your own name as its author!
   4. Add the `dependencies` field. Our project will depend on the `pandas` library, so add it to the list.
   5. Let's add the `build-system` section. Just like the example, the `requires` field should have `setuptools>=61.0` as its value and the `build-backend` field should have `setuptools.build_meta` as its value.
   6. Add the `tool.setuptools` section. It should have the `packages` field with `life_expectancy` as its value. **Without this field, Python won't be able to find your package**.
3. Install its dependencies on editable mode with `pip install -e '.[dev]'`.
4. Finally, run the tests again. They should now **pass**.

## Submitting your assignment

If everything is working, you should do your first commit and push it to GitHub.

To push your code to GitHub, you can either do this [directly from VSCode](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git#_publish-local-repository-to-github) or you can create the repo on GitHub and then follow their instruction on how to push an existing repository.

If your repository is private, don't forget to add your mentor and pod colleages as a collaborators.
