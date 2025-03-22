typecheck:
	pipenv run mypy .

format:
	pipenv run ruff format .

lint:
	pipenv run ruff check . --fix

run:
	pipenv run daphne -b 0.0.0.0 -p 8000 movie_poster_classifier.asgi:application

makemigrations:
	pipenv run python manage.py makemigrations

migrate:
	pipenv run python manage.py migrate

test:
	pipenv run pytest movie_poster_classifier/tests