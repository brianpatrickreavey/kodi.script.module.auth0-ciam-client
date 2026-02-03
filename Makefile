# Makefile for kodi.script.module.auth0-ciam-client addon development
SHELL := /bin/bash

.PHONY: clean-addon help install test unittest-with-coverage reinstall-kodi-checker validate

# Default target
help:
	@echo "Available targets:"
	@echo "  install                - Set up the development environment (create .venv and install dependencies)"
	@echo "  test                   - Run unit tests"
	@echo "  unittest-with-coverage - Run unit tests with coverage report"
	@echo "  reinstall-kodi-checker - Reinstall kodi-addon-checker package"
	@echo "  validate               - Run Kodi addon validation with custom mirror domain"
	@echo "  clean-addon            - Clean addon directory of Python artifacts"
	@echo "  help                   - Show this help message"

# Installation
install:
	uv sync --group dev

unittest-with-coverage:
	pytest --cov=resources --cov-report=term-missing tests/

reinstall-kodi-checker:
	uv cache clean && uv sync --reinstall-package kodi-addon-checker

validate:
	KODI_CHECKER_DIR=$$(find .venv -name kodi_addon_checker -type d | head -1); \
	cp kodi_addon_checker/check_addon.py $$KODI_CHECKER_DIR/; \
	cp kodi_addon_checker/__main__.py $$KODI_CHECKER_DIR/; \
	cp kodi_addon_checker/addons/Repository.py $$KODI_CHECKER_DIR/addons/; \
	uv run kodi-addon-checker --addon-repo-domain mirror.umd.edu --branch matrix --enable-debug-log --reporter console --reporter log script.module.auth0-ciam-client/

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
