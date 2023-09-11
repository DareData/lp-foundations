# The `pyproject.toml` file

Ever stumbled upon the mysterious "Relative import" error? Or wondered why you can't just use your scripts everywhere? Let's unravel these mysteries with `pyproject.toml`.

## Scripts vs. Packages

- **Script**: A standalone Python file (or Jupyter Notebook). It's like a solo singer
- **Package**: A collection of Python files that play well together.

There is a big difference between directly running a Python file and importing that file from a package. When you're working in a notebook (like a Jupyter notebook) or running a script, Python sees it from a specific location on your computer but it may not know where your imports are.

> If your script/notebook is inside a folder, it might not easily recognize or access files in the **parent directory** or **folders above** it. 😵‍💫
>
> But it will be able to access files in the **same folder** or **folders below** it. 🤗

To solve this, you must either restructure your project or tell Python where to look for the files you want to import. There are 3 ways to do this:

- **The crazed way**: Restructure your project so that all imports come from its sibling modules. **This is a TEMPORARY solution. Only do this for throwaway code, like experiment notebooks that reuse some code**.
- **The dirty, not at all recommended way**: You can add the parent directory to the `sys.path` list. This is a list of directories that Python searches when looking for files to import. You can add a directory to this list with `import sys sys.path.append("..")`. This is not recommended because it can cause problems if you have multiple files with the same name in different directories. It's also not very clear to other people reading your code.
- **The clean, recommended way**: You can turn your code into a package. 🎉
  - It's a more structured solution. This means organizing your code in a way that Python recognizes it as a cohesive unit.
  - Install it locally in editable mode: this means any changes you make to the package are immediately reflected when you use it. **By installing it this way, Python will automatically add it to its path, making it easily accessible from anywhere, including your notebook**.

This approach not only solves the import issue but also makes your code more organized and modular. It's a more professional way to manage and use your code.

## Let's Get Packaging! 📦

That's what `pyproject.toml` is for. It's a configuration file that tells Python how to build and package your project. It's the blueprint for your package. It's also the new standard for Python projects and includes:

- **Build System**: How to build your project.
- **Metadata**: Information about your project.
- **Dependencies**: Packages your project depends on.
- **Tool Settings**: Settings for tools used in your project.
- **Scripts**: Scripts to run your project.

## Why can I just use `requirements.txt`?

- **`requirements.txt`**: The old shopping list 🛍️. Just a list of dependencies.
- **`pyproject.toml`**: The modern blueprint 🏰. A configuration file for building, packaging, and distributing Python projects.

### Why the Shift?

`pyproject.toml` was introduced as a response to the limitations of the older tools. The Python community wanted:

1. **Unified Configuration**: One file to rule them all.
2. **Flexibility**: More control over how projects are built and packaged.
3. **Clarity**: Clearer ways to specify dependencies and metadata.

It's now the canonical way of doing things, backed by [`PEP 518`](https://peps.python.org/pep-0518/) and [`PEP 621`](https://peps.python.org/pep-0621/).

## Crafting Your `pyproject.toml` 🛠️

### Mandatory Fields

- **`[build-system]`**: Tells tools how to build your project.
  - `requires`: List of packages needed to build yours.
  - `build-backend`: The backend system used to build the package.

- **`[project]`**: Describes your project.
  - `name`: Your package's name.
  - `version`: Your package's version.

### Optional (But Cool) Fields

- `description`: A short description of your project.
- `authors`: Who's behind this awesome package?
- `dependencies`: List of packages your project depends on.
- `readme`: The README file for your project.
- `requires-python`: The Python version your project requires.

### Example

```toml
[project]
name = "my_cool_package"
version = "0.1.0"
description = "A cool package doing cool things."
authors = [{name="Your Name", email="you@example.com"}]
dependencies = ["requests", "numpy==1.19.2"]

readme = "README.md"
requires-python = ">=3.7"

# These are optional. For example we usually use a `dev` section for dev dependencies
# like testing libraries. You final users won't need them, but you, as the developer,
# might.
[project.optional-dependencies]
dev = ["pytest", "pylint", "pytest-cov"]

# This bit is important. It tells Python how to build your project.
# In this case, we're using setuptools, which is usually already
# included in your Python installation.
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

# This is also important. It tells setuptools which packages to include.
# If you don't add this, you won't be able to import your package, 
# (`import my_cool_package`) even if you install it.
[tool.setuptools]
packages = ["my_cool_package"]
```

Please note the `packages` option. It assumes your project is structured like this:

```bash
project_directory/
├── pyproject.toml
├── README.md
└── my_cool_package/
    ├── __init__.py
    └── example.py
```

If you have a different structure, you have to let your `pyproject.toml` file know where it can find your package. Each build tool will have its own syntax for this, but you can always consult the documentation. For example, here's the one for [`setuptools`](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

### Installing 💪

Once you have your `pyproject.toml` file, you can install your package in editable mode with:

```bash
# Remember to active your virtual environment first!
pip install -e '<path_to_your_pyproject>[optional dependency groups]'
```

The `-e` argument means "editable". This means that any changes you make to your package will be immediately reflected when you use it. This is great for development, but you should remove it when in production or when running from a CI/CD pipeline.

So if you have a `dev` dependency group and your terminal is at the project root, the command would be:

```bash
pip install -e '.[dev]'
```

Or if you don't have any optional dependencies, just:

```bash
pip install -e .
```

Boom! You can now import your package without errors! 👌

## Wrapping Up 🎉

With `pyproject.toml`, you're not just writing code; you're crafting an experience! 🌈
Embrace it, and those pesky "Relative import" errors will be a thing of the past.
