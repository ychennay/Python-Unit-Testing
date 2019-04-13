from pytest import fixture
import time

class DatabaseConnection():

    id = 0
    def __init__(self):
        time.sleep(1) # simulates some costly network connection

        DatabaseConnection.id += 1
        self.connection = f" CONNECTION #{DatabaseConnection.id}"

@fixture(scope="session")
def connection():
    yield DatabaseConnection()

    print("Running tear down code!")