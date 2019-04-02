#########
# Tasks #
#########
.PHONY: clean build run stop inspect

IMAGE_NAME = alefh/alpine-python3-speed-racer
CONTAINER_NAME = speed-racer

# Build local project
#
#   make build
#
build/local: build/dependencies/install build/dependencies/lib/safety-check build/code-style run

# Build local project
#
#   make build
#
build: build/dependencies/install build/dependencies/lib/safety-check build/code-style docker/build/image docker/run

# Run pep8 code style validations
#
#   make build/code-style
#
build/code-style:
	$(PYTHON_BIN)/pycodestyle --statistics --ignore=E501,W605 --count application/ domain/ infrastructure/ test/

# Install dependent libraries
#
#   make build/dependencies/install
#
build/dependencies/install:
	$(PYTHON_BIN)/pip3 install -r build_requirements.txt
	$(PYTHON_BIN)/pip3 install -r requirements.txt

# Run safety check on lib dependencies
#
#   make build/dependencies/lib/safety-check
#
build/dependencies/lib/safety-check:
	echo "checking the libs of production requirements ..."
	$(PYTHON_BIN)/safety check -r requirements.txt
	echo "checking the libs of tests requirements ..."
	$(PYTHON_BIN)/safety check -r build_requirements.txt

# Create image of app
#
#   make build/image
#
docker/build/image:
	docker build -t $(IMAGE_NAME) .

# Run the container with app
#
#   make docker/run
#
docker/run:
	docker run -d -p 3000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop running container of app
#
#   make docker/stop
#
docker/stop:
	docker stop $(CONTAINER_NAME)

# Access shell of running container
#
#   make docker/stop
#
docker/shell:
	docker exec -it $(CONTAINER_NAME) /bin/sh

# Clean docker services of app
#
#   make docker/clean
#mak
docker/clean: docker/stop
	docker ps -a | grep '$(CONTAINER_NAME)' | awk '{print $$1}' | xargs docker rm \
	docker images | grep '$(IMAGE_NAME)' | awk '{print $$3}' | xargs docker rmi

# Run project tests
#
#   make test
#
test: build/local test/run

# Run tests
#
#   make test/run
#
test/run:
	$(PYTHON_BIN)/py.test test --no-print-logs

# Run app standalone
#
#   make test/run
#
run:
	$(PYTHON_BIN)/python app.py

# Setup the local development environment with python3 .env and project dependencies
#
#   make setup/environment
#
setup/environment:
	echo "create virtualenv environment to python 3.7 ..."
	virtualenv .env -p peython3


###############
# Definitions #
###############

CURRENT_BRANCH = $(shell git rev-parse --abbrev-ref HEAD)
PYTHON_BIN ?= .env/bin
