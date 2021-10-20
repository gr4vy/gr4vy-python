
lint:
	poetry run isort --check-only .
	poetry run black --check .

test:
	poetry run pytest -vv