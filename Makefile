DIST?=centos7

all: rpm

rpm:
	docker-compose run --rm $(DIST)

clean:
	rm -rf rpm/

.PHONY: rpm clean
