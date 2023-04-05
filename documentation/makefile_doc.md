```pytest -vvv -rf -q --cov --cov-report term $(PY_MODULES) $(PYTESTFLAGS)```

The pytest command runs the pytest testing framework on the specified modules.
The -vvv flag sets the verbosity level to "very very verbose", which means that pytest will print a lot of information about each test.
The -rf flag shows "only failed tests and any important information", suppressing the output for passing tests.
The -q flag suppresses extra information when running tests.
The --cov flag enables code coverage measurement with pytest-cov.
The --cov-report term flag specifies that coverage statistics should be printed to the terminal in a simple format.
The $(PY_MODULES) variable should contain a space-separated list of Python module file paths to be tested by pytest.
The $(PYTESTFLAGS) variable can contain additional command-line flags and options to be passed to pytest.

So when you run make test-unit, it will execute the pytest command with the specified options, running the unit tests and measuring code coverage for the specified modules.


```
test-mypy:  # typing check
	mypy $(PY_MODULES)
```
Here's how it works:

The target is test-mypy.
The command to run is mypy $(PY_MODULES).
The mypy command runs the mypy tool on the specified modules.
The $(PY_MODULES) variable should contain a space-separated list of Python module file paths to be checked by mypy.
So when you run make test-mypy, it will execute the mypy command on the specified modules, checking for type errors and inconsistencies in your Python code.


```test-isort:
	isort -l80 -m3 -c --tc $(PY_MODULES)
```

Here's how it works:

- The target is test-isort.
- The command to run is isort -l80 -m3 -c --tc $(PY_MODULES).
- The isort command checks the import order of the specified modules.
- The -l80 flag sets the line length to 80 characters.
- The -m3 flag sets the multi-line import style to "vertial hanging indent".
- The -c flag makes isort only check the import order and not apply any changes.
- The --tc flag prints a unified diff of the changes that would be made by isort.
- The $(PY_MODULES) variable should contain a space-separated list of Python module file paths to be checked by isort.
So when you run make test-isort, it will execute the isort command on the specified modules, checking their import order against the specified style rules and printing a diff of any changes that would be made.