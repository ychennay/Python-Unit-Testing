from pytest import mark
import logging

@mark.database
def test_driver():
    print("Testing Driver")
    assert True

@mark.database
def test_engine():
    logging.info("Testing engine.")
    assert True

@mark.database
@mark.react_component
def test_frontend_db_gui():
    assert True