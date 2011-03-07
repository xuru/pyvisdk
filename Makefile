PYTHON?=python
SETUPFLAGS=
TESTRUNNER = $(shell which nosetests)

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
	-rm -rf api_docs/

help:
	@echo 'Commonly used make targets:'
	@echo '  all          - build program and documentation'
	@echo '  install      - install program and man pages to PREFIX ($(PREFIX))'
	@echo '  install-home - install with setup.py install --home=HOME ($(HOME))'
	@echo '  local        - build for inplace usage'
	@echo '  tests        - run all tests in the automatic test suite'
	@echo '  test-foo     - run only specified tests (e.g. test-merge1)'
	@echo '  dist         - run all tests and create a source tarball in dist/'
	@echo '  clean        - remove files created by other targets'
	@echo '                 (except installed files or dist source tarball)'
	@echo '  update-pot   - update i18n/hg.pot'
	@echo
	@echo 'Example for a system-wide installation under /usr/local:'
	@echo '  make all && su -c "make install" && hg version'
	@echo
	@echo 'Example for a local installation (usable in this directory):'
	@echo '  make local && ./hg version'

apidocs: apidocs_html apidocs_pdf

apidocs_html: 
	epydoc --html --config epydoc.conf

apidocs_pdf: 
	epydoc --pdf --config epydoc.conf 
	mv api_docs/api.pdf api_docs/dogtail.pdf

.PHONY: help all inplace build clean apidocs apidocs_html apidocs_pdf
