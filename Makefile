.PHONY: clean virtualenv test install

PYTHON_PATH := $(shell which python3)

test:
		python -m pytest \
		    -v \
		    --cov=myapp \
		    --cov-report=term \
		    --cov-report=html:coverage-report \
		    tests/

clean:
		find . -name '*.py[co]' -delete

virtualenv:
		virtualenv --python="$(PYTHON_PATH)" --prompt=="|> W2O <|" src/env
		src/env/bin/pip3 install -r requirements.txt
		src/env/bin/pip3 freeze | sed -ne 's/==.*//p' | xargs src/env/bin/pip3 install -U
		@echo
		@echo "Virtualenv created, use 'source src/env/bin/activate' to use it"
		@echo

install:
		sudo apt-get -y install python-virtualenv python3-dev
