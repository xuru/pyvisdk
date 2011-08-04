PYTHON?=python
SETUPFLAGS=
TESTRUNNER=$(shell which nosetests)
API_DOC_DIR=docs/html

all: build

build:
	$(PYTHON) ./bootstrap.py -d
	./bin/buildout
	PYTHONPATH=. $(PYTHON) setup.py $(SETUPFLAGS) build

test:
	PYTHONPATH=. $(PYTHON) ./bin/test

install:
	PYTHONPATH=. $(PYTHON) setup.py $(SETUPFLAGS) install


clean:
	-find . \( -name '*.o' -o -name '*.so' -o -name '*.py[cod]' -o -name '*.dll' \) -exec rm -f {} \;
	-rm -rf pyvisdk.egg-info eggs develop-eggs parts build dist docs/html

help:
	@echo 'Commonly used make targets:'
	@echo '  all          - build program and documentation'
	@echo '  test         - run all tests in the automatic test suite'
	@echo '  docs         - generate all the documentation'
	@echo '  install      - Install the python module'
	@echo '  clean        - remove files created by other targets'
	@echo '                 (except installed files or dist source tarball)'

docs: 
	rm -rf $(API_DOC_DIR)
	./bin/sphinx-build -b html docs docs/html

.PHONY: help all build test clean docs
