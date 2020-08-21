up: build
	docker-compose up -d

build:
	mkdir -p src/finsee/db
	docker-compose build

setup: build up
	docker-compose exec finsee ./manage.py createsuperuser

stop:
	docker-compose down
	docker-compose stop

clean: stop
	docker-compose rm

rebuild: clean build up