# Makefile for kodi.script.module.auth0-ciam-client addon development
SHELL := /bin/bash

.PHONY: clean-addon help

# Default target
help:
	@echo "Available targets:"
	@echo "  clean-addon - Clean addon directory of Python artifacts"
	@echo "  help        - Show this help message"

# Clean addon directory
clean-addon:
	find script.module.auth0-ciam-client -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find script.module.auth0-ciam-client -type f -name "*.pyc" -delete 2>/dev/null || true