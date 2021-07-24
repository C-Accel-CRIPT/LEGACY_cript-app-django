# CRIPT app

This repository stores the web application for CRIPT: the Community Resource for Innovation in Polymer Technology.




## Setup
1. Create a new directory to store the project in, navigate to the directory, and create a virtual environment inside it: `python3 -m venv venv`
1. Activate the virtual environment: `source venv/bin/activate`
	* To install packages into the virtual environment: `pip install -r requirements.txt`
    * To export packages from the virtual environment: `pip freeze > requirements.txt`
    * To deactivate the virtual environment: `deactivate`
1. To run the project, navigate inside the directory with `manage.py` and use `python manage.py runserver`. The page will be viewable at `http://127.0.0.1:8000`
	* To quit the server, use `control-c`
1. After making changes to models, the models can be "migrated" to the database using `python manage.py makemigrations`; `python manage.py migrate`



#### Creating a new app inside the project

1. in the directory with `manage.py`, create a new app using `python manage.py startapp baseapp` where `baseapp` is the name of the app
1. create a view for the app in `baseapp/views.py`
1. map the view to a URL using a `URLconf`. this should be in `baseapp/urls.py`
1. now we need to point the root `URLconf` at the `baseapp.urls` module. In `dsite/urls.py`, add an import for `django.urls.include` and insert the app in the urlpatterns list