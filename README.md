
# What?

That's a package to run tests about basics of Python.
For example, lists, strings, for, dictionaries, ...

# Installing

$ mkdir venv-damebasics
$ python3 -m venv venv-damebasics
$ cd venv-damebasics
$ source bin/activate
$ pip3 install damebasics

# Run tests!

All tests
$ cd damebasics
$ ./runtests.sh

Single file of tests
$ pytest tests/test_arithmetics.py

Single test
$ pytest tests/test_arithmetics.py::TddInPythonExample::test_arithmetics_calculator_returns_correct_result

# Give me the package

<https://python-packaging.readthedocs.io/en/latest/minimal.html>

To install from local: 
$ pip install -e .

To install create tar.gz in dist directory: 
$ python3 -m build

To upload to pypi: 
$ twine upload dist/damebasics-0.2.tar.gz


