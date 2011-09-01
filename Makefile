PYTHON?=python
SETUPFLAGS=
TESTRUNNER=$(shell which nosetests)
API_DOC_DIR=docs/html
PROJ_DIR=`pwd`
VERSION=0.9

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

update_version:
	sed -i "s/^__version__ = .*/__version__ = \'$(VERSION)\'/g" pyvisdk/__init__.py

release: clean build docs deploy_docs
	echo "============================================================"
	echo " Release complete "
	echo "============================================================"

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
	./bin/docs

deploy_docs:
	ghp-import -m "Updated documentation for version $(VERSION)" -p docs/build/html

.PHONY: help all build test clean docs
