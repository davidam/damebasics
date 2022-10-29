
# What?

That's a package to run tests about basics of Python.
For example, lists, strings, for, dictionaries, ...

# Run tests!

$ ./runtests.sh

# Give me the package

<https://python-packaging.readthedocs.io/en/latest/minimal.html>

To install from local: 
$ pip install -e .

To install create tar.gz in dist directory: 
$ python3 setup.py register sdist

To upload to pypi: 
$ twine upload dist/damebasics-0.0.1.tar.gz

To install from Internet: 
$ pip3 install damebasics

If you upload various tar.gz to pypi, you can need remove old files in dist directory and repeat the process:
$ rm dist/\*tar.gz
$ python3 setup.py register sdist
$ twine upload dist/damebasics-0.0.1.tar.gz

