
# Makefile for deltadefi-python-sdk (uv-managed Python project)
# Usage examples:
#   make install       # create venv and install project + dev deps
#   make test          # run pytest
#   make fmt lint      # format + lint with Ruff
#   make build         # build the package
#   make help          # list targets

SHELL := /bin/bash
.DEFAULT_GOAL := help

UV := uv
PY := python

.PHONY: help venv install fmt lint type test cov build clean docs deps

help: ## Show this help with grouped commands
	@echo "Available commands:"
	@echo ""
	@echo "📦 Installation & Setup:"
	@grep -E '^[a-zA-Z_\-]+:.*##.*install' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "🔧 Testing & Quality:"
	@grep -E '^[a-zA-Z_\-]+:.*##.*\[(test|lint|format|type|quality|check)\]' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "🏗️  Building & Distribution:"
	@grep -E '^[a-zA-Z_\-]+:.*##.*\[(build|dist)\]' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "📚 Other Utilities:"
	@grep -E '^[a-zA-Z_\-]+:.*##[^[]*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

# 📦 Installation & Setup
venv: ## Create virtual environment [install]
	@$(UV) venv

install: ## Install project in editable mode with dependencies [install]
	@$(UV) pip install -e . --group dev --group docs

deps: install ## Install dependencies (alias for install) [install]

# 🔧 Testing & Quality
fmt: ## Format code with Ruff formatter [format]
	@$(UV) run ruff format .

lint: ## Lint with Ruff (auto-fix + fail on remaining issues) [lint]
	@$(UV) run ruff check --fix --exit-non-zero-on-fix .

type: ## Static type-check with mypy [type]
	@$(UV) run mypy --config-file=pyproject.toml src/ || true

test: install ## Run tests with pytest [test]
	@$(UV) run pytest -vv

cov: install ## Check code coverage [test]
	@$(UV) run pytest -n 4 --cov deltadefi

cov-html: cov ## Check code coverage and generate HTML report [test]
	@$(UV) run coverage html -d cov_html
	@echo "Coverage report generated in cov_html/"

# 🏗️  Building & Distribution
build: install ## Build the package [build]
	@$(UV) build

# 📚 Other Utilities
docs: install ## Build the documentation
	@mkdir -p docs/requirements
	@$(UV) export --group docs > docs/requirements.txt
	@rm -r -f docs/build
	@$(UV) run sphinx-build docs/source docs/build/html
	@echo "Documentation built in docs/build/html/"

clean-test: ## Remove test and coverage artifacts
	@rm -f .coverage
	@rm -fr cov_html/
	@rm -fr .pytest_cache

clean: clean-test ## Remove caches, build artifacts, and temp files
	@rm -rf .mypy_cache .ruff_cache dist build
	@find . -type d -name __pycache__ -prune -exec rm -rf {} +

version: ## Show uv and Python versions
	@$(UV) --version
	@$(UV) run $(PY) -c "import platform; print('Python', platform.python_version())"

precommit-install: ## Install pre-commit hooks
	@$(UV) run pre-commit install

precommit: ## Run pre-commit hooks on all files
	@$(UV) run pre-commit run --all-files

precommit-update: ## Update pre-commit hooks
	@$(UV) run pre-commit autoupdate
