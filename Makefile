.PHONY: build test publish
now := $(shell date -u +"%Y-%m-%dT%H:%M:%SZ")
commit := $(shell git rev-parse --short HEAD)

publish: test
	docker push 192.168.1.10:32000/remote:latest
	docker push 192.168.1.10:32000/remote:$(commit)

test: build
	true

build:
	docker build -t 192.168.1.10:32000/remote:$(commit) -t 192.168.1.10:32000/remote:latest --build-arg now=$(now) --build-arg commit=$(commit) .
