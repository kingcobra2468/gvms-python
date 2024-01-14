.PHONY: build dist redist install install-from-source clean uninstall

build:
	./setup.py build

dist:
	./setup.py sdist bdist_wheel

redist: clean dist

install:
	pip3 install .

install-from-source: dist
	pip3 install dist/gvms-1.0.0.tar.gz

clean:
	$(RM) -r build dist src/*.egg-info
	$(RM) -r src/gvms/file/*.c
	$(RM) -r .pytest_cache
	find . -name __pycache__ -exec rm -r {} +

test: install-from-source
	pip3 install "gvms[test]"
	python3 -m pytest --tests-per-worker 4

uninstall:
	pip3 uninstall gvms