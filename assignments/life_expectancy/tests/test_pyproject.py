"""
Unit tests for the pyproject.toml file.

It's very uncommon to write unit tests for a configuration file. However,
since we are learning, this is a special case.

Once you have ensured that the package and its dependencies are installed,
feel free to delete this file.
"""
from pkg_resources import DistributionNotFound, get_distribution

import toml
import pytest
import pylint
import pytest_cov
import pandas as pd

from . import PROJECT_DIR


def test_dependencies():
    """Test that the get_versions function return 4 values."""
    deps = (
        pd.__version__,
        pytest.__version__,
        pytest_cov.__version__,
        pylint.__version__
    )
    assert len(deps) == 4


def test_pyproject():
    """Test that the pyproject.toml is correct."""
    pyproject = toml.load(PROJECT_DIR / "pyproject.toml")

    authors = pyproject["project"]["authors"]
    has_new_author = False
    for author in authors:
        if not author["name"].startswith("Fernando Cordeiro"):
            has_new_author = True

    assert pyproject["project"]["name"] == "life_expectancy"
    assert has_new_author, (
        "The author of the package is not Fernando Cordeiro. You should "
        "add your own name to the pyproject.toml file."
    )


def test_package():
    """Test that the life_expectancy package is installed."""
    try:
        installed_package = get_distribution("life_expectancy")
    except DistributionNotFound:
        assert False, (
            "The life_expectancy package is not installed. If you have "
            "installed the package, check that the name of the package "
            "in the pyproject.toml file is `life_expectancy`."
        )
    assert installed_package.version == "0.1.0", (
        "The life_expectancy package is installed, but it is not the "
        "correct version. If you have installed the package, check "
        "that the version of the package in the pyproject.toml file "
        "is `0.1.0`."
    )
