install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff

build: 
	poetry build
