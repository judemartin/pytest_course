from contextlib import closing

import pytest

from some_db import DB


@pytest.fixture()
def db():
    with closing(DB()) as db:
        yield db


# using a context manager to create and close the DB object
def test_db(db):
    result = db.some_action()
    assert result == 42
