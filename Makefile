all: rpm

rpm:
	docker-compose run --rm centos7

clean:
	rm -rf rpm/

.PHONY: rpm clean
