.PHONY: build test publish
now := $(shell date -u +"%Y-%m-%dT%H:%M:%SZ")
commit := $(shell git rev-parse --short HEAD)

publish: test
	docker push alexcreek/remote:latest
	docker push alexcreek/remote:$(commit)

test: build
	true

build:
	docker build -t alexcreek/remote:$(commit) -t alexcreek/remote:latest --build-arg now=$(now) --build-arg commit=$(commit) .
