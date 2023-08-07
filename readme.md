# Installation

```Bash
python3 -m venv place
source place/bin/activate
pip install django
django-admin startproject marketplace

```
# Server starten 

`python manage.py runserver`

# Erste Django App

- `python manage.py startapp core`
- in settings.py INSTALLED_APPS muss angepasst werden.

## erste view erstellen

- in core/views.py 
- templates ordner muss auf app-ebene erstellt werden.
- im ordner templates den core ordner anlegen
- dort die index.html bearbeiten
- dann die datei zu den urls.py hinzufügen
- neue html-datei mit dem dateinamen base.html erstellen
- Mit `{% extends 'core/base.html'%}` wird die index.html kreiert
- nachdem html-seiten gemacht sind: neue app 'item'
- dann anpassen der models.py
- dann `python manage.py makemigrations`
- dann `python manage.py migrate`


## Admin anlegen

`python manage.py createsuperuser`

- eigene urls.py datei für items, ist sauberer


bis zur suche