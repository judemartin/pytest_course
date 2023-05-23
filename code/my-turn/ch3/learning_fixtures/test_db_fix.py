import pytest

from some_db import DB


@pytest.fixture()
def db():
    db = DB()  # setup resource
    yield db  # yield resource
    db.close()  # teardown: close resource


def test_db(db):
    result = db.some_action()
    assert result == 42
