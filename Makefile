.PHONY: build run

build:
	python -m pipenv install

run:
	python -m pipenv run main.py