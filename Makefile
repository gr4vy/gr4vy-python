
lint:
	poetry run isort --check-only .
	poetry run black --check .

test:
	pytest -vv test_gr4vy.py