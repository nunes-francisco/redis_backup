# Nome do arquivo: Makefile

# Variáveis
PYTHON := python3
PIP := $(PYTHON) -m pip
FORMATTERS := black isort
LINTER := flake8

# Alvos

.PHONY: all
all: install format lint

.PHONY: install
install:
	$(PIP) install --upgrade pip
	$(PIP) install $(FORMATTERS) $(LINTER)

.PHONY: format
format:
	$(PYTHON) -m black .
	$(PYTHON) -m isort .

.PHONY: lint
lint:
	$(PYTHON) -m flake8 .

.PHONY: check
check:
	$(PYTHON) -m black --check .
	$(PYTHON) -m isort --check-only .
	$(PYTHON) -m flake8 .

.PHONY: clean
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
