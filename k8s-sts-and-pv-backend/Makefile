##############################################################################
# Targets

VERSION := $(shell cat VERSION)

IMAGE_REPO_PREFIX := ""
IMAGE_REPO_BASENAME := $(shell basename $(CURDIR))
IMAGE_REPO := $(IMAGE_REPO_PREFIX)$(IMAGE_REPO_BASENAME):$(VERSION)


##############################################################################
# Targets

.PHONY: clean
clean:
	docker builder prune -f


.PHONY: build
build:
	DOCKER_BUILDKIT=1 docker build \
		--tag $(IMAGE_REPO) \
		--no-cache \
		./
