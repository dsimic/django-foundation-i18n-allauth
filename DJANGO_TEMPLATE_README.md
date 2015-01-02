## Django bootstrap project template
### Includes
* Zurb Foundation 5
* django-annoying
* django-static
* django-debug-toolbar
* django-extensions
* django-allauth

### How to use
Create virtual environment, change project_name with your projects name :D
```sh
mkvirtualenv project_name
```

Install django
```sh
pip install django
```

Run django startproject with the --template option
```sh
django-admin.py startproject --template=https://github.com/dsimic/django-foundation-i18n-allauth/archive/master.zip project_name
```

Install requirements, for development
```sh
pip install -r requirements/development.txt
```

Make django static dir, from project root:
```sh
mkdir -p project_name/public/django-static/static
```

Create your own LICENSE.md and README.md to suite your project needs.

Set 'PROJECT_ENV' environment variable.
* 'development'
* 'production',
* 'staging'

If no 'PROJECT_ENV' especified takes 'development' settings as default

For development environment:
```sh
sudo sh -c 'echo "export PROJECT_ENV=development" >> /etc/profile.d/environment.sh' && source /etc/profile.d/environment.sh
```
Done.

Inspired by https://github.com/netoxico/django-bootstrap.
