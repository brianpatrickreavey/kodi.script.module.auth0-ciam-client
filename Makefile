# Makefile for kodi.script.module.auth0-ciam-client addon development
SHELL := /bin/bash

.PHONY: clean-addon help install test unittest-with-coverage validate

# Default target
help:
	@echo "Available targets:"
	@echo "  install                - Set up the development environment (create .venv and install dependencies)"
	@echo "  test                   - Run unit tests"
	@echo "  unittest-with-coverage - Run unit tests with coverage report"
	@echo "  validate               - Run kodi-addon-checker. BRANCH defaults to matrix. Example: make validate BRANCH=nexus"
	@echo "  clean-addon            - Clean addon directory of Python artifacts"
	@echo "  help                   - Show this help message"

# Installation
install:
	uv sync --group dev

# Tests mock xbmc. They do not start Kodi.
test:
	uv run pytest tests/ -q

unittest-with-coverage:
	uv run pytest --cov=resources --cov-report=term-missing tests/

# BRANCH is a kodi-addon-checker version name: matrix, nexus, omega, or piers.
BRANCH ?= matrix

validate:
	uv run kodi-addon-checker --branch $(BRANCH) script.module.auth0-ciam-client/

# Cleanup
clean:
	rm -rf dist/ build/ *.egg-info/
	rm -rf .pytest_cache/ .coverage htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Clean addon directory
clean-addon:
	find script.module.auth0-ciam-client -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find script.module.auth0-ciam-client -type f -name "*.pyc" -delete 2>/dev/null || true
