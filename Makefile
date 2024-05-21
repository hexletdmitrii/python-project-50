install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

build: 
	poetry build

#test-coverage:
#	poetry run pytest --cov

selfcheck:
	poetry check

check: selfcheck test lint

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

