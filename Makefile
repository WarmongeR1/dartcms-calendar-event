BASEDIR=$(CURDIR)

pip-tools:
		pip install pip
		pip install pip-tools

requirements: pip-tools
		pip-compile requirements/base.in
		pip-sync requirements/base.txt

test:
		py.test apps agents utils tests helpers

static:
		python manage.py collectstatic --noinput

.PHONY: test