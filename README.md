DartCMS Boilerplate
===================

This repository contains empty DartCMS-based application.
You can clone it, change repository settings in your `.git/config` file and start coding your project.

Quickstart
----------

- Edit your hosts file. Add entry for your website: `127.0.0.1 example.dev admin.example.dev`
- Clone repository
- Cd into project root
- Change git repository settings
- Setup1 database
- Change `conf.dev.project_settings` and `conf.prod.project_settings` according to your needs
- Run `virtualenv --no-site-packages --prompt="(your project name)" venv && source venv/bin/activate`
- Run `pip install -r ./requirements/base.txt` to setup all deps.
- Run `python manage.py migrate`
- Create Django's superuser: `python manage.py createsuperuser`
- Run `python manage.py runserver`
- Navigate your browser to `http://admin.example.dev:8000/admin/modules/module/` and setup DartCMS module rights for your superuser

# TODO последний шаг не сработал сразу
# TODO добавить пояснение, как потом соединять в основным проектом
# TODO нужен набор фикстур для dartcms

What's next
-----------

- Read DartCMS documentation to write new apps - http://dartcms.readthedocs.io/en/latest/
- If you want to contribute, feel free to fork repo and create pull-request!