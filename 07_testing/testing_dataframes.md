# Testing Dataframes

Testing data transformation in Python slightly differs from testing normal functions and methods. The good news, however, is that they almost always follow the same structure. The bad news is that structure requires you to create data fixtures: files in CSV, JSON, or even Python tuples/dictionary containing data samples

The structure of the test will always be the same: we want to load a fixture (read: fake testing data) mimicking the input table(s) into dataframes, then load another fixture mimicking the expected output, and finally we run the code we want to test to see if the actual output matches the expected output. This means comparing data frame equality.

## Pandas dataframes

Comparing data frame equality in pandas is straightforward. We can simply leverage the pandas' testing submodule. The two functions we'll be using the most are assert_frame_equal and assert_series_equal.

Here's an example using the pytest framework:

```python
from pathlib import Path

import pandas as pd

from my_code import my_function

FIXTURE_DIR = Path(__file__).parent.joinpath("fixtures")

def test_my_function():
    # Given the input data and expected output...
    input_df = pd.read_json(f"{FIXTURE_DIR}/input_data.json")
    expected = pd.read_json(f"{FIXTURE_DIR}/output_data.json")
    # When we run the function...
    actual = my_function(input_df)
    # Then we expect the output to match the expected output
    pd.testing.assert_frame_equal(actual, expected)
```

If you see yourself repeating the same fixture loading code over and over again, you can create a fixture function. Pytest has a reserved module called `conftest.py` where you can define fixtures that will be available to all tests in the same directory and subdirectories. Here's an example:

```python
# conftest.py
from pathlib import Path

import pandas as pd
import pytest

FIXTURE_DIR = Path(__file__).parent.joinpath("fixtures")

@pytest.fixture
def input_df():
    return pd.read_json(f"{FIXTURE_DIR}/input_data.json")

@pytest.fixture
def expected():
    return pd.read_json(f"{FIXTURE_DIR}/output_data.json")


# test_my_code.py
from my_code import my_function

def test_my_function(input_df, expected):
    actual = my_function(input_df)
    pd.testing.assert_frame_equal(actual, expected)
```

This helps you to reduce the amount of code you need to write for each test. It also helps you to keep your tests DRY (Don't Repeat Yourself).

### Mock Pandas read functions

Since a Unit Test is supposed to be an "isolated unit of code", it means that the code should be able to run itself without relying on external services or system, including expectations of what is on the file system or database. Any services or files loaded by the code should be "mocked" so that the unit test can run without relying on it. This will result in an independent test suite that can be executed anywhere.

"Mocking" is the concept of replacing a real call to something (could be code, a file, a query, a response, etc.) with a fake, pre-defined response. This results in the following benefits:

- You do not rely on the external code or service.
- You speed up your test. It does not need to do IO or computations that are outside the scope of the test.
- You can predict the response. If the code generates random values, uuid's, timestamps etc., you can make turn those responses into static, predetermined values.

Some developers get confused by this, how can we ensure that a function that queries a database is working as expected if we hardcode the response of the query? Well, the point of our unit test isn't to test if the database connection is working, if the table exists or if its data is correct. All you care about is the logic that is within the "unit" of code you just wrote.

Let's see an example! Imagine you've just wrote this function:

```python
# my_code.py
import pandas as pd

def get_df():
    df = pd.read_sql("SELECT * FROM foo;", connection)
    return df.rename({"foo_id": "bar_id"})

```

Notice how it uses uses Pandas' built-in `read_x` functions to read in the data from an external source, in this case, an SQL database.

We do not care about testing the underlying SQL connection to the database. We trust that the `read_sql` function works provided to us by the pandas library. We also trust that the connection object works as expected, and even if it is something written by ourselves in-house, there should be other tests that would test the database python module used.

So what do we want to test?

- Does the function attempt to query a database with the expected SQL query?
- Does the function rename the columns?
- Does the function return a dataframe?

We can achieve this with the following test:

```python
from unittest.mock import patch, Mock

@patch("my_code.pd.read_sql")
def test_get_df(read_sql_mock: Mock):
    read_sql_mock.return_value = pd.DataFrame({"foo_id": [1, 2, 3]})
    results = get_df()
    read_sql_mock.assert_called_once()
    
    pd.testing.assert_frame_equal(results, pd.DataFrame({"bar_id": [1, 2, 3]}))

```

In this case, we use the `patch` as a decorator instead of as a context manager. When we use it as a decorator it automatically creates a mock that gets passed into the test function as an argument.

As you can see from the test, by mocking the `read_sql` function we are able to achieve the following:

- Remove any dependency of an SQL database from our test.
- We make our test more readable since we can see inside the test what the dataframe returned from the `read_sql` function will be.
- Our test becomes an "isolated unit of code" that we test. We do not care about the other functions that the function is calling in nested ways, we only test the functionality that is limited to the `get_df` function.

## Pyspark dataframes

Testing equality on Pyspark dataframes is trickier because the pyspark library offers no helper functions. So we must create our own. I usually put mine inside a `tests/asserts.py` file. Here's an example (it's a bit long, sorry!):

```python
# asserts.py
import logging

from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql import functions as F
from pyspark.sql.types import DoubleType


def assert_sdf_equal(
    df1: SparkDataFrame, df2: SparkDataFrame, check_nullable=True, precision: int = None
) -> None:
    """
    Asserts that two Spark DataFrames are equal in terms of schema and data.

    Args:
        df1 (SparkDataFrame): The first Spark DataFrame to compare.
        df2 (SparkDataFrame): The second Spark DataFrame to compare.
        check_nullable (bool, optional): Whether to check if nullable
            columns match. Defaults to True.
        precision (int, optional): The number of decimal places to round 
            double columns to. Useful when comparing FloatType columns. 
            Defaults to None.

    Raises:
        AssertionError: If the two DataFrames are not equal in terms of schema and data.
    """
    assert _is_schema_equal(df1, df2, check_nullable)

    if precision:
        df1 = _round_double_cols(df1, precision)
        df2 = _round_double_cols(df2, precision)
    assert _is_data_equal(df1, df2)


def _is_data_equal(df_actual: SparkDataFrame, df_expected: SparkDataFrame) -> bool:
    # Handle duplicated rows
    if df_actual.count() != df_expected.count():
        return False

    # We sort the columns so that column order does not matter
    df_actual = df_actual.select(sorted(df_actual.columns))
    df_expected = df_expected.select(sorted(df_expected.columns))

    # Flatten data so that StructType columns can be compared
    df_actual_flat = _flatten_df(df_actual)
    df_expected_flat = _flatten_df(df_expected)

    try:
        except_all = df_actual_flat.exceptAll(df_expected_flat)
    except AttributeError:
        # In spark 2.3 and below, we can't use exceptAll, so we use an anti-join
        except_all = df_actual_flat.join(
            df_expected_flat, on=df_actual_flat.columns, how="leftanti"
        )
    return except_all.count() == 0


def _flatten_df(df: SparkDataFrame) -> SparkDataFrame:
    """Flatten all nested columns in a SparkDataFrame

    We need to do this because Spark does not compare nested columns
    when comparing DataFrames.
    """
    flat_cols = [F.col(c) for c, t in df.dtypes if t[:6] != "struct"]
    nested_cols = [c[0] for c in df.dtypes if c[1][:6] == "struct"]

    flat_df = df.select(
        flat_cols
        + [
            F.col(nc + "." + c).alias(nc + "_" + c)
            for nc in nested_cols
            for c in df.select(nc + ".*").columns
        ]
    )
    return flat_df


def _is_schema_equal(
    df1: SparkDataFrame, df2: SparkDataFrame, check_nullable=True
) -> bool:
    """Check if two Spark DataFrames have the same schema
    
    This is useful for making the dataframe comparison faster, as we can
    skip the data comparison if the schemas are different.
    """
    def field_list(fields):
        return fields.name, fields.dataType, fields.nullable

    fields1 = {field_list(field) for field in df1.schema.fields}
    fields2 = {field_list(field) for field in df2.schema.fields}

    if check_nullable:
        res = set(fields1) == set(fields2)
    else:
        res = {field[:-1] for field in fields1} == {field[:-1] for field in fields2}
    return res


def _round_double_cols(df: SparkDataFrame, scale: int) -> SparkDataFrame:
    """
    Round all Double type columns in a datafram to scale decimal places using
    HALF_UP rounding mode if scale >= 0 or at integral part when scale < 0.
    """

    for col_name in df.columns:
        if not isinstance(df.schema[col_name].dataType, DoubleType):
            continue
        df = df.withColumn(col_name, F.round(F.col(col_name), scale))
    return df
```

And then we can use that to test our data frames:

```python
from pyspark.sql import SparkSession as spark

from my_code import my_function
from .asserts import assert_sdf_equal

def test_my_function():
    # Given the input data and expected output...
    input_df = spark.createDataFrame([{"name": "Alice", "age": 1}])
    expected = spark.createDataFrame([{"name": "Alice", "year_born": 1974}])
    # When we run the function...
    actual = my_function(input_df)
    # Then we expect the output to match the expected output
    assert_sdf_equal(actual, expected)
```

By the way, did you notice the comments in the examples? They are there to draw your attention on how we usually structure our tests. It's called the Arrange-Act-Assert pattern and you rand read more about it [here](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/).

### Mocking the spark session

Let's talk about the SparkSession in your tests. Imagine that the function you want to test is querying the Spark cluster, like this:

```python
# my_code

from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql import SparkSession

def my_function() -> SparkDataFrame:
    # First collect the data
    spark = SparkSession.getActiveSession()
    df = spark.sql("select * from table;")

    # Then we perform a bunch of filters and calculation
    ...


    # Finally, we return the new data frame
    return df
```

With some very few exceptions, one doesn't want to connect to the actual databases when testing data transformation. Some reasons are:

- We don't want to depend on internet availability and database permissions in order to run tests;
- We don't want our tests to change any actual data by accident;
- We don't want our tests competing for computing resources (and those resources might be expensive!).

For that reason, we will have to replace the actual connection with a "fake" one. This is called mocking. We want to create a mock of the SparkSession object so that, when it calls the `sql` method, it returns our input fixture data instead of actually querying the database.

With pytest, creating mocks is relatively simple:

```python
# conftest.py
import pytest
from pyspark.sql import SparkSession

# We give it the scope "session" so that it only creates a new spark session once
@pytest.fixture(scope="session")
def spark() -> Generator[SparkSession, None, None]:
    # This creates a local spark session. The 1 represents how many
    # partitions it should create. Ideally, this value should be the 
    # number of CPU cores you have.
    spark = SparkSession.builder.master("local[1]").appName("tests").getOrCreate()

    # The reason we use a yield statement instead of a return statement
    # is because we want to ensure the spark session is stopped after
    # all tests are done.
    # we use the yield statement to tell pytest to run the tests, and
    # then return to this point and continue executing the rest of the
    # code in this funtion.
    yield spark

    # This code will run after all tests are done
    spark.stop()
```

Now any test that receives spark_session as an argument will be able to use a local spark session. The scope argument tells pytest this variable should exist throughout the test suite. Had we not added it, pytest would create a new local spark session before every test.

But we are not done yet. We still need to replace the `sql` call without fixture data. We do that with the `unittest.mock.patch decorator`. When we use this decorator, we have to add an extra argument to the test function definition. That argument can have any name. Because we are patching the `sql` method, I'll be calling it `patched_sql`.

The final form of the test is as follows:

```python
from unittest.mock import patch

from pyspark.sql import SparkSession as spark

from my_code import my_function
from . import assert_sdf_equal

@patch("my_code.SparkSession.sql")
def test_get_sellout_banner_filter(patched_sql, spark_session):
    # Given the input data and expected output...
    input_df = spark_session.createDataFrame([{"name": "Alice", "age": 1}])
    expected = spark_session.createDataFrame([{"name": "Alice", "year_born": 1974}])
    # When my_function calls the spark.sql method, we want it to return the input_df.
    patched_sql.return_value = input_df
    # So that when we run the function...
    actual = my_function(spark_session)
    # Then we expect the output to match the expected output
    assert_sdf_equal(actual, expected)
```

Note that, because `my_function` gets a spark session by using the `getActiveSession` method instead of creating a one, it will use the `spark` mock we have created instead of connecting the remote spark cluster.

If `my_function` were instead either creating a new spark session or receiving it from somewhere else, we would have to change the test structure in order to ensure we would be using a mock session.
