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


@mark.business_logic
class AggregationLanguageTests:

    def test_group_by(self, connection):
        logging.info(f"Testing group by components with {connection.connection}")
        assert True

    @mark.database
    def test_window_function(self):
        assert True