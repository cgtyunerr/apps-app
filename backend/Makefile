SHELL=/bin/bash
.DEFAULT_GOAL := default

.PHONY: install
install:
	@echo "Installing Production Dependencies."
	pip install poetry
	poetry install


.PHONY: coverage
coverage:
	@echo "Test coverage."
	bash scripts/test.sh

.PHONY: run
run:
	@echo "Running the application."
	poetry run uvicorn src.main:app --reload

