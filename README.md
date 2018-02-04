# Weavedin-Library-WebApp
A web application for a library system using django and materialize css

### frameworks used:
* django
* Materialize css

### database used:
*mysql

### to run:
1. clone the repository
`git clone https://github.com/sherinann/Weavedin-Library-WebApp`

2. install dependencies
 * django
` pip install django `
  * sql client
  `pip install mysqlclient`
  
3. add database credentials to `settings.py`

4. create superuser
   `python manage.py createsuperuser`
5. make migrations and migrate
  `python manage.py makemigrations
  python manage.py migrate`
6. run the server
  `python manage.py runserver`
7. go to: http://127.0.0.1:8000
  



