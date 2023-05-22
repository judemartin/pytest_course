# Getting started with Pytest

1. `python3 --version` # check python version (root directory)
2. `python3 -m venv venv --prompt .` # create virtual environment (root directory)
3. `source venv/bin/activate` # activate virtual environment (root directory)
4. `pip list` # list installed packages (root directory)
5. `which pip` # check pip location, should be in venv (root directory)
6. `pip install -U pip` # upgrade pip (root directory)
7. `pip install pytest` # install pytest (root directory)
8. `pip install ./cards_proj` # install package (code directory)
9. `python3 --version` # check python version (root directory)
10. `pytest --version` # check pytest version (root directory)
11. `cards version` # check package version` (root directory)
12. `which python3` # check python location, should be in venv
13. `which pytest` # check pytest location, should be in venv
14. `pytest` # run tests  (my-turn directory),  


# Cards 
1. `cards add do something --owener Jude` # add card (my-turn directory)
2. `cards add do somethine else` # add card (my-turn directory)
3. `cards` # list cards (my-turn directory)
4. `cards config` # list config (my-turn directory)
5. `cards update 2 --owner Jude` # update card (my-turn directory)
6. `cards` # list cards (my-turn directory)
7. `cards start 1`
8. `cards` # list cards (my-turn directory)
9. `cards finish 1`
10. `cards start 2` # list cards (my-turn directory)
11. `cards` # list cards (my-turn directory)
12. `cards delete 1` # delete cards (my-turn directory)
13. `cards` # list cards (my-turn directory)


# Pytest
1. `pytest --version` # check pytest version (root directory)
2. `pytest` # run tests  (my-turn directory),
3. `pytest -v` # run tests with verbose output (my-turn directory),
4. `pytest -v -s` # run tests with verbose output and print statements (my-turn directory),
5. `pytest -v test_card.py` # run specific tests based on file name in from ch2 dir (my-turn/ch2 directory),
6. `pytest -v test_classes.py` # run test contained in class
7. `pytest -v test_classes.py::TestEquality::test_equality_with_diff_ids` # run a single test contained in class `(copy from the test output)`
8. `pytest -v test_classes.py::TestEquality` # run all the tests contained it the class TestEquality.
9. ` pytest --tb=no` # Test summary from pytest, run inside the `my-turn/ch2` directory, tb is for traceback
10. `pytest --tb=no -k fail -v` # run tests that contain the word fail in the name, -k is for keyword      
11. `pytest --tb=no -k "not fail" -v` # run tests that do not contain the word fail in the name, -k is for keyword (keyword with logic)
12. `pytest --tb=no -k "equal and not fail" -v` # there are two keywords, equal and not fail, (create any number of combinations with logic) _(run handful of tests)_