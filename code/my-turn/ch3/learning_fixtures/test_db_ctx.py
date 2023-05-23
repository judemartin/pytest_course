from contextlib import closing
from some_db import DB


# using a context manager to create and close the DB object
def test_db():
    with closing(DB()) as db:
        result = db.some_action()
        assert result == 42
