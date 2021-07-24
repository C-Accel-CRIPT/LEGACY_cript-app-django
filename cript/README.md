# CRIPT app

This repository stores the web application for CRIPT: the Community Resource for Innovation in Polymer Technology.


## Description of files

* `manage.py`: command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
* The inner `cript/` directory is the actual CRIPT Python package. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `cript.urls`).
    * `/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
    * `c/settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
    * `/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
    * `/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
    * `/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

The CRIPT application is built from smaller applications.
* `api` is the CRIPT API application   
* `search` is the CRIPT search application


