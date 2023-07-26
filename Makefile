.ONESHELL:

.DEFAULT_GOAL := run
TOPICS := fix - feat - docs - style - refactor - test - chore - build


PYTHON = ./.venv/bin/python3
PIP = ./.venv/bin/pip

.PHONY: run clean help commit format branch lint

help:
	@echo "gmake help - display this help"
	@echo "gmake branch - create a new branch"
	@echo "gmake build - create and activate virtual environment"
	@echo "gmake clean - remove all generated files"
	@echo "gmake commit - commit changes to git"
	@echo "gmake format - format the code"
	@echo "gmake lint - run linters"
	@echo "gmake run - run the application"

branch:
	@echo "Available branch types:"
	@echo "$(TOPICS)"
	@read -p "Enter the branch type: " type; \
	read -p "Enter the branch description (kebab-case): " description; \
	git checkout -b $${type}/$${description}; \
	git push --set-upstream origin $${type}/$${description}

build: venv/bin/activate
	. ./.venv/bin/activate

clean:
	@echo "Cleaning up..."
	@find . -name "__pycache__" -type d -exec rm -rf {} +
	@find . -name ".pytest_cache" -exec rm -rf {} +
	@find . -name ".venv" -exec rm -rf {} +	

commit: format
	@echo "Available topics:"
	@echo "$(TOPICS)"
	@read -p "Enter the topic for the commit: " topic; \
	read -p "Enter the commit message: " message; \
	git add .; \
	git commit -m "$${topic}: $${message}"; \
	git push

format: 
	$(PYTHON) -m black .

lint:
	$(PYTHON) -m flake8 
	$(PYTHON) -m pylint **/*.py **/**/*.py *.py

mongostart:
	@echo "Starting MongoDB..."
	brew services start mongodb-community@6.0

mongostop:
	@echo "Stopping MongoDB..."
	brew services stop mongodb-community@6.0

run: build
	$(PYTHON) app.py

venv/bin/activate: requirements.txt
	python3 -m venv .venv
	$(PIP) install -r requirements.txt