# Foundations Learning Path Assignments

## Introduction

We are going to be using this project throughout the course.

This assignment uses life expectancy in Europe grouped by Country (or other, like group of countries), Age, Sex, and Time. But the data format makes it hard to use. We will be building a pipeline do clean the data, while applying the concepts you've learned in the previous modules.

## Installing

Before installing, make sure your `pip` is up to date.

```bash
pip --version
```

Prior to the introduction of `pyproject.toml`-based builds (in PEP 517 and PEP 518), pip had only supported installing packages using setup.py files that were built using `setuptools`. But in version 21.3, pip added support for performing editable installs of packages that use `pyproject.toml`. This means that you can use pip to install packages described in the `pyproject.toml`.

To update pip, run:

```bash
pip install --upgrade pip
```

Now you're ready to go!

1. Clone this repo.
2. Copy `assignments` folder into a separate project `mv -r nos-lp-foundations/assignments assignments`.
3. Move into the assignments folder (`cd assignments`) and start a new repo (`git init`).
4. Create a virtual environment with `python -m venv .venv`.
   > **Note for Anaconda users**: We would prefer if you exit the automatic conda environments and tried using the steps above, as they are the canonical Python way of creating virtual environments. However, we realize working that way might be tricky for Anaconda users since Anaconda usually changes the configurations of your machine. If you are having too many problems getting started, then feel free to use the "conda way" of handling environments.  I.e.: create a virtual environment with `conda create --name foundations`.
5. Activate the virtual environment with `source .venv/bin/activate` or `.venv\Scripts\activate` on Windows.
   > **Note for Anaconda users**: Same as above, if you are having too many problems getting started, then feel free to activate the environment with `conda activate foundations` instead.

Don't install the project yet. We will do that in [setup assignment](./assignment_0/README.md).

## Using this project

Open the `README.md` file inside each assignment and follow the instructions.

> Note: Remember that all commands inside the Readme files assume you are in the root of the project.

You can now start working on the [setup assignment](./assignment_0/README.md). Good luck! 🚀
