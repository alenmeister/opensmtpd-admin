PROJECT_NAME := $(shell basename $(PWD))
VIRTUAL_ENV := $(pipenv --venv --quiet)

define HELP
Manage $(PROJECT_NAME). Usage:

make run - Run $(PROJECT_NAME) locally
make install - Create local virtualenv and install dependencies
make deploy - Install project and run locally
make update - Update dependencies via pipenv
make clean - Remove extraneous compiled files, caches, logs, etc.

endef
export HELP


.PHONY: run install deploy update clean help

all help:
	@echo "$$HELP"

.PHONY: run
run:
	pipenv run uwsgi --http :5000 --wsgi-file wsgi.py --callable app

.PHONY: install
install:
	pipenv install --dev --python 3.11

.PHONY: deploy
deploy:
	make install && \
	make run

.PHONY: update
update: 
	pipenv run pip install --upgrade pip setuptools wheel && \
	pipenv update

.PHONY: clean
clean:
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete
	@find . -name '*.log' -delete
	@find . -name '.DS_Store' -delete
	@find . -wholename '**/*.pyc' -delete
	@find . -type d -wholename '__pycache__' -exec rm -rf {} +
	@find . -type d -wholename '.pytest_cache' -exec rm -rf {} +
	@find . -type d -wholename '**/.pytest_cache' -exec rm -rf {} +
	@find . -type d -wholename '**/*.log' -exec rm -rf {} +
	@find . -type d -wholename '**/.webassets-cache' -exec rm -rf {} +
