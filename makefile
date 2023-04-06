PY_MODULES=src test
CONFIGFILE=setup.cfg
DOCKER_REGISTRY=sshukla
IMAGE_NAME=myspark
IMAGE_TAG=3.7-3.10
DOCKER_WORKDIR=/tmp
DOCKER_ARGS=-v $(PWD):$(DOCKER_WORKDIR) -w $(DOCKER_WORKDIR) -u root

#----------- Tests -------------------------------------------------------------
# When you run `make test`, it will execute the test command, which will run following tests
# test-unit: pytest -vvv -rf -q --cov --cov-report term $(PY_MODULES) $(PYTESTFLAGS)

#------------------------------------------------------------------------
test:
	@$(PRE_ACTIVATE) $(MAKE) -j4 --no-print-directory \
		test-unit \
		test-black \
		test-isort \
		test-pylint \
		test-mypy

test-black: # code formatter
	black --check -l 80 $(PY_MODULES)

test-mypy:  # typing check
	mypy $(PY_MODULES)

test-pylint:
	pylint -f parseable \
		--rcfile=${RCFILE} \
		-j 4 \
		$(PY_MODULES)

unittest:
	python -m unittest discover tests/

coverage:
	coverage run --source=. -m unittest discover tests/
	coverage report --fail-under=80
	coverage html

test-isort:
	isort -l80 -m3 -c --tc $(PY_MODULES)


#----------- DEV ---------------------------------------------------------------

black: ## Format all the python code
	black -l 80 $(PY_MODULES)

isort: ## Sort imports in the python module
	isort -l80 -m3 --tc $(PY_MODULES)

#------------ PACKAGING  -------------------------------------------------------

package:
	package.sh

#------------ RUN/DEBUG  -------------------------------------------------------
run:
	spark-submit \
	--jars jars/spark-excel_2.11-0.9.9.jar \
	--py-files datajob.zip \
	datajob/cli.py \
	--job-name demo_job

#------------ DOCKER -----------------------------------------------------------
build-docker: ### Build the docker image
	docker build .\
	  -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} \
	  -f docker/dev.Dockerfile

test-docker:
	docker run --rm \
	  ${DOCKER_ARGS} \
	  ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} \
	  make test-unit

run-docker:
	docker run -it \
	  ${DOCKER_ARGS} \
	  ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} \
	  /bin/bash -c "make package; make run"

#------------ MISC -----------------------------------------------------------
intall-py-deps:
	poetry config virtualenvs.create false && poetry install
