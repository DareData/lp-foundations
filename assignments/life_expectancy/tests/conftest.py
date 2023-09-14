"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR


@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run.

    1. Everything you may write before 'yield' will run before the tests
    2. The command 'yield' marks where tests will happen
    3. The code after 'yield' will be run after the tests are finished.

    Before you start using your own fixtures, all tests will produce a csv file
    on the output directory. Since this is bad practise, we are erasing this
    file to avoid polluting your workspace.

    After refactoring your functions this code will do nothing.
    """
    # Setup: fill with any logic you want

    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)


@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")
