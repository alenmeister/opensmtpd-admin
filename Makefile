PROJECT_NAME := $(shell basename $(PWD))
VIRTUAL_ENV := $(PWD)/.venv
LOCAL_PYTHON := $(VIRTUAL_ENV)/bin/python3

define HELP
Manage $(PROJECT_NAME). Usage:

make run - Run $(PROJECT_NAME) locally
make install - Create local virtualenv and install dependencies
make deploy - Install project and run locally
make update - Update dependencies via pipenv and output resulting `Pipfile`
make clean - Remove extraneous compiled files, caches, logs, etc.

endef
export HELP


.PHONY: run install deploy update clean help

all help:
	@echo "$$HELP"

env: $(VIRTUAL_ENV)

$(VIRTUAL_ENV):
	if [ ! -d $(VIRTUAL_ENV) ]; then \
		echo "Creating Python virtual env in \`${VIRTUAL_ENV}\`"; \
		python3 -m venv $(VIRTUAL_ENV); \
	fi

.PHONY: run
run: env
	$(LOCAL_PYTHON) -m flask run

.PHONY: clean
clean:
	find . -name '.coverage' -delete && \
	find . -name '*.pyc' -delete && \
	find . -name '__pycache__' -delete && \
	find . -name '*.log' -delete && \
	find . -name '.DS_Store' -delete && \
	find . -wholename '**/*.pyc' -delete && \
	find . -wholename '**/*.html' -delete && \
	find . -type d -wholename '__pycache__' -exec rm -rf {} + && \
	find . -type d -wholename '.venv' -exec rm -rf {} + && \
	find . -type d -wholename '.pytest_cache' -exec rm -rf {} + && \
	find . -type d -wholename '**/.pytest_cache' -exec rm -rf {} + && \
	find . -type d -wholename '**/*.log' -exec rm -rf {} + && \
	find . -type d -wholename './.reports/*' -exec rm -rf {} +
