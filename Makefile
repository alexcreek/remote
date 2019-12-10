.PHONY: build
now := $(shell date -u +"%Y-%m-%dT%H:%M:%SZ")
commit := $(shell git rev-parse HEAD)

build:
	docker build -t remote --build-arg now=$(now) --build-arg commit=$(commit) .
