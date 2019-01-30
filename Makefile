KVKV_ENV ?= local
KVKV_PORT ?= 9099
KVKV_HOST ?= 0.0.0.0

app := app
project := proj

pipenv := pipenv

python3 := ${pipenv} run env NERU_ENV=${KVKV_ENV} python3
manage_py := ${python3} manage.py


runserver:
	${manage_py} $@ '${KVKV_HOST}:${KVKV_PORT}'

migrate:
	${manage_py} $@
