# Advanced Testing Features

### Using Markers


#### Single Markers
You can decorate your Pytests to provide finer-grain control of execution. For example, in the `test_database.py` file, the `test_driver` function test is marked with `@mark.database`.

```python
@mark.database
def test_driver():
    print("Testing Driver")
    assert True
```

You can execute only tests marked as `database` by invoking `pytest -m database` from the command line.

#### Multiple Markers

You can use boolean OR / AND logic to trigger different combinations of tests:

`pytest -m "database or react_component"` will select all tests that are marked with either `database` or `react_component`. `pytest -m "database and react_component` will run all tests marked with both.

Running `pytest -m "not database"` will run all tests that are not marked with `database`.