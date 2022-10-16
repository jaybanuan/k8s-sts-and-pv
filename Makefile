##############################################################################
# Targets

VERSION := $(shell cat VERSION)


##############################################################################
# Targets

.PHONY: clean
clean:
	$(MAKE) -C k8s-sts-and-pv-web clean
	$(MAKE) -C k8s-sts-and-pv-backend clean


.PHONY: build
build:
	$(MAKE) -C k8s-sts-and-pv-web build
	$(MAKE) -C k8s-sts-and-pv-backend build
