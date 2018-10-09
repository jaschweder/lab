.PHONY: all clean docker-build docker-run

DOCKER=docker
DOCKER_IMAGE=jaschweder/swig
DOCKER_RUN=$(DOCKER) run -it --rm -v $(PWD):/go/src -w /go/src $(DOCKER_IMAGE)

all : docker-build
	$(DOCKER_RUN) sh -c 'cd ./example && swig -go -cgo -intgosize 32 example.i && go install'

run :
	$(DOCKER_RUN) go run main.go

docker-build :
	$(DOCKER) build -t $(DOCKER_IMAGE) .

docker-run :
	$(DOCKER_RUN) bash

