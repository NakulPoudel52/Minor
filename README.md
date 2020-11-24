# Minor
This project is for the fulfillment of degree in bachelor in computer engineering.
sagarmatha engineering college.

We have used python framework called django for backend and postgresql as database.
For frontend HTML,CSS,JS and Bootstrap is used.

steps for running application

1. pip3 install -r requirements.txt [To install all dependencies]
2.Install postgres sql for database.
3.Install the additional module pg_trgm.
	

	a) Log into postgres

	psql -U <DB_USERNAME>

	b) After you are connected, switch to the DB you want to install the extension for:

	\c <DB_NAME>

	c) Then install the extension as answered previously:

	CREATE EXTENSION pg_trgm;

	Installing the extension initially gave me issues because I was not doing step b. I thought the installation was a global thing but it seems its per DB
Reference:
https://dba.stackexchange.com/questions/165300/how-to-install-the-additional-module-pg-trgm.
for setting up database use
python manage.py make migrations
python manage.py migrate

Finally launch django application using
python manage.py runserver
