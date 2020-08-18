## Simple Django Rest Boilerplate

### How to run:
```
1. Clone or download the project in your local
2. Create a virtualenv inside the root directory. (you can create this via `virtualenv --python=python3 venv`)
1. Activate the venv by `source venv/bin/activate`. This command is for Linux. See your OS command from internet
1. Install the required packages via `pip install -r requirements.txt`
1. Create a (mysql) database in your database server. You can do this via command prompt or 'mysql work bench'
1. Create an .env file inside the root directory like mentioned above and set proper value
1. Makemigrations via `python manage.py makemigrations`
1. Migrate that 'migrations file'  via `python manage.py migrate`
1. Run the project via `python manage.py runserver`
1. Now test the api via postman or direct hit the url from browser.
1. URL list:
    Get all: http://localhost:8000/api/device-info/tokens/
    Get specific one: http://localhost:8000/api/device-info/tokens/<specific_id_here>
    Post: http://localhost:8000/api/device-info/tokens/

```