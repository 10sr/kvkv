# KVKV_ENV ?= local
KVKV_PORT ?= 9099
KVKV_HOST ?= 0.0.0.0
KVKV_SQLITE3 ?= ${CURDIR}/db.sqlite3
export KVKV_SQLITE3

app := app
project := proj

pipenv := pipenv
poetry := poetry

python3 := ${pipenv} run python3
manage_py := env KVKV_ENV=${KVKV_ENV} ${python3} ./manage.py


.PHONY: ${MAKECMDGOALS}

runserver:
	${manage_py} $@ '${KVKV_HOST}:${KVKV_PORT}'

migrate:
	${manage_py} $@

create_admin_user:
	${manage_py} $@


#########
# black

black:
	${pipenv} run black .

black-check:
	${pipenv} run black --check .
