## Simple Django Rest Boilerplate

### Demo .env

```
SECRET_KEY="lftg45yerdgdf834y29(86as9$a2tmqkend"
DEBUG=True
DATABASES_NAME="your database name"
DATABASES_USER="database uer"
DATABASES_PASSWORD="database password"
DATABASES_HOST='localhost'
DATABASES_PORT='3306'
API_URL=""
STATIC_ROOT=""
MASTER_MODULE_API_URL=""
USER_MODULE_API_URL=""
PRODUCT_MODULE_API_URL=""
MEDIA_BASE_DIR=""
JWT_SECRET_KEY="dev_wlrjfsea1"
JWT_VALID="3600"
TIME_ZONE="Asia/Dhaka"
ALLOWED_HOSTS="localhost"
```

### How to run:
```
1. Clone or download the project in your local
2. Create a virtualenv inside the root directory. (you can create this via `virtualenv --python=python3 venv`)
3. Activate the venv by `source venv/bin/activate`. This command is for Linux. See your OS command from internet
4. Install the required packages via `pip install -r requirements.txt`
5. Create a (mysql) database in your database server. You can do this via command prompt or 'mysql work bench'
6. Create an .env file inside the root directory like mentioned above and set proper value
7. Makemigrations via `python manage.py makemigrations`
8. Migrate that 'migrations file'  via `python manage.py migrate`
9. Run the project via `python manage.py runserver`
10. Now test the api via postman or direct hit the url from browser.
11. URL list:
    Get all: http://localhost:8000/api/device-info/tokens/
    Get specific one: http://localhost:8000/api/device-info/tokens/<specific_id_here>
    Post: http://localhost:8000/api/device-info/tokens/

```
