
VIRTUALENV_DIR ?= env

help:
	@echo "run test - run tests quickly with the default Python"
	@echo "run coverage - run coverage quickly with the default Python"

BASE_DIR = .

BUILD_DIR = $(BASE_DIR)/build
DIST_DIR = $(BASE_DIR)/dist

clean:
	-rm -rf $(BUILD_DIR)
	-rm -rf $(DIST_DIR)

release: clean report
	python3 setup.py bdist_wheel

tests:
	$(VIRTUALENV_DIR)/bin/python -m unittest discover

coverage:
	$(VIRTUALENV_DIR)/bin/python -m coverage run -m unittest discover


report: coverage
	pip install -r requirements.test.txt
	coverage report --omit=$(VIRTUALENV_DIR)/*,examples/*,tests/*
	coverage html --omit=$(VIRTUALENV_DIR)/*,examples/*,tests/*
	coverage xml --omit=$(VIRTUALENV_DIR)/*,examples/*,tests/*

dev:
	pip install -r requirements.test.txt
	pip install -e .
