# Workshop-1
## Project setup

- `cd workshop1` 
- `python3 -m venv workshop1`
- `source workshop1/bin/activate`
- `pip install -r requirements.txt`

## Start Develop
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver 0.0.0.0:8000`
- `go to url 0.0.0.0:8000/home`
## init data
- `python manage.py loaddata cactusshopdb/cactusshop.json`
 