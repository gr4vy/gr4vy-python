
lint:
	poetry run isort --check-only --skip="gr4vy/gr4vy_api" --skip=".venv" .
	poetry run black --check --exclude="gr4vy/gr4vy_api|.venv" . 

lint-apply:
	poetry run isort --skip="gr4vy/gr4vy_api" --skip=".venv" .
	poetry run black --exclude="gr4vy/gr4vy_api|.venv" . 

test:
	poetry run pytest -vv test_gr4vy.py