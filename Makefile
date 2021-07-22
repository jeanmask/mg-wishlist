# This file is part of Poetry
# https://github.com/python-poetry/poetry

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2018 Sébastien Eustace

POETRY_RELEASE := $$(sed -n -E "s/__version__ = '(.+)'/\1/p" poetry/__version__.py)


clean:
	@rm -rf build dist .eggs *.egg-info
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

format: clean
	@poetry run pre-commit run -a -v black
	@poetry run pre-commit run -a -v isort

test:
	@poetry run pytest -xs

build:
	@poetry build

publish:
	@poetry publish

wheel:
	@poetry build -v
