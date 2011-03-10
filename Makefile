PYTHON?=python
SETUPFLAGS=
TESTRUNNER=$(shell which nosetests)
API_DOC_DIR=apidocs

all: inplace

# Build in-place
inplace:
	PYTHONPATH=. $(PYTHON) setup.py $(SETUPFLAGS) build_ext --inplace

build:
	PYTHONPATH=. $(PYTHON) setup.py $(SETUPFLAGS) build

debug:
	PYTHONPATH=. $(PYTHON) setup.py $(SETUPFLAGS) build_ext --pyrex-gdb --inplace

test:
	PYTHONPATH=. $(PYTHON) $(TESTRUNNER) test

clean:
	-find . \( -name '*.o' -o -name '*.so' -o -name '*.py[cod]' -o -name '*.dll' \) -exec rm -f {} \;
	-rm -rf build dist
	-rm -rf apidocs/

help:
	@echo 'Commonly used make targets:'
	@echo '  all          - build program and documentation'
	@echo '  test         - run all tests in the automatic test suite'
	@echo '  docs         - generate all the documentation'
	@echo '  clean        - remove files created by other targets'
	@echo '                 (except installed files or dist source tarball)'

docs: 
	rm -rf $(API_DOC_DIR)
	epydoc --html --config epydoc.conf
	tar czf apidocs.tar.gz apidocs/

.PHONY: help all inplace build test clean docs
