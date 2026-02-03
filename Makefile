# Makefile for kodi.script.module.auth0-ciam-client addon development
SHELL := /bin/bash

.PHONY: clean-addon help test unittest-with-coverage

# Default target
help:
	@echo "Available targets:"
	@echo "  test                   - Run unit tests"
	@echo "  unittest-with-coverage - Run unit tests with coverage report"
	@echo "  clean-addon            - Clean addon directory of Python artifacts"
	@echo "  help                   - Show this help message"

# Testing
test:
	pytest tests/ -v

unittest-with-coverage:
	pytest --cov=resources --cov-report=term-missing tests/

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
