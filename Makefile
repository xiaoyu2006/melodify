.PHONY: help install dev lint dist clean

help:
	@echo "install - install (dev) dependencies"
	@echo "dev - run Melodify"
	@echo "lint - run pylint"
	@echo "dist - build Melodify using pyinstaller"
	@echo "clean - remove build artifacts"

install:
	poetry install --with dev

dev: install
	poetry run melodify

lint: install
	poetry run pylint --recursive=y melodify

dist: install
	poetry run pyinstaller --name="Melodify" --windowed executable.py

clean:
	rm -rf ./build ./dist ./__pycache__ */**.spec *.spec
