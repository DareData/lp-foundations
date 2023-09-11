# Get started with Python in VS Code (0h20)

The first thing you need after installing VS Code is to install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python). This extension is the official Python plugin for VS Code and it provides a lot of useful features.

The second thing you need to do is to select a Python interpreter. 9 out of 10 times your get a `ModuleNotFound` error is because you are using the wrong interpreter. The Python extension will try to detect the interpreter for you, but you can also select it manually.

Make sure you read about deal with environments and the Python interpreter in VS Code: [VSCode docs: Environments](https://code.visualstudio.com/docs/python/environments)

## Setting up VS Code for Python development (0h10)

### Configuration

VSCode is highly customizable. This customization lives in the `.vscode/settings.json` file and can be altered either in that file directly or via the user interface.

> Make sure you have added the `.vscode/` directory to the `.gitignore` file, so your settings don't end up polluting the Git repository by mistake.

Here are some useful settings:

---

```json
"editor.rulers": [88, 120]
```

Render vertical rulers after a certain number of monospace characters. Use multiple values for multiple rulers. Useful in order to ensure no line is too long.

---

```json
"python.testing.pytestEnabled": true OR false,
"python.testing.unittestEnabled": true OR false,
```

Helps VSCode identify the Python testing framework being used: pytest vs. unittest.

---

```json
"python.analysis.typeCheckingMode": strict
```

Defines the default rule set for type checking. Options are:

- `off` - no type checking,
- `basic` - More lenient checker. Useful for when working with some external libraries (like Pandas, for instance),
- `strict` - Shows you any error that happens with typing.

---

```json
"editor.formatOnSave": true
```

Formats files when they are saved. This allows your code to follow a consistent style automatically. In order to to this, you will need a formatter, like [black](https://github.com/psf/black). There's usually a different formatter for each code style. If you need more information about code styles, it's useful to read a few examples. For example, [Google's Python styleguide](https://google.github.io/styleguide/pyguide.html) is publicly available. The next setting will allow you to choose a formatter.

---

```json
"python.formatting.provided": "black",
```

Option to determine how VSCode should format your code. Possible formatters are `Black`, `Autopep8`, and `Yapf`.

---

```json
"editor.formatOnSaveMode": "file"
```

This controls how the file will be formatted. Options are:

- `file` - formats entire file,
- `modifications` - formats only what was modified (requires version control),
- `modificationsIfAvailable` - attempts to format only what was modified, but if version control is not available, formats the entire file.

---

```json
"editor.codeActionsOnSave": ["source.organizeImports"]
```

VSCode allows for other actions to be performed when the file is saved. Each action should be added to the list and will be executed in order. The most popular action is `source.organizeImports` which sorts the file imports.

---

```json
"python.linting.pylintEnabled": true,
"python.linting.enabled": true,
```

`python.linting` is where the linting options live. The Python extension supports `Pylint`, `bandit`, `pylama`, `Pydocstyle`, `Pycodestyle`, `Prospector`, `Mypy`, and `Flake8`.

## Recommended plugins, Tasks and the Test Explorer

[Link to document](https://docs.google.com/document/u/1/d/1xHJ9Kq9OVsWh4OH8DYB_7dsKW2tzCPZ8FOI9VrGU2SU)

This document helps you setup VS Code's Test Explorer, Tasks. It also provides some plugins recommendations.
