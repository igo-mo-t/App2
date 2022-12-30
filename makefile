test:
	python -m pytest -s

build:
	docker-compose -f docker-compose.yml up --build

lint:
	flake8 app


