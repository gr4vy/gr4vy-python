test:
	poetry run pytest tests

lint:
	poetry run pylint -j=0 tests src  

setup: deps

deps:
	poetry install

.PHONY: setup lint test deps