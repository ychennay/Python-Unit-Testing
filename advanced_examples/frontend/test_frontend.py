from pytest import mark
import logging
logging.basicConfig(level=logging.INFO)

@mark.react_components
def test_react_components(connection):
    logging.info(f"Testing React components with {connection.connection}")
    assert True