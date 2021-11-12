docker-build:
	docker build -t coderetreat2021 .

docker-clean:
	docker rm -f coderetreat2021

docker-test: docker-clean docker-build
	docker run --name coderetreat2021 coderetreat2021 make test

run:
	python3 -m app

check-linting:
	cd src; mypy --strict .
	cd src; find . -name *.py | xargs pylint

test:
	cd src; pytest -v ./tests