Introduction
============
The assignment consists of a web server containing both the backend and frontend and a database.

The REST API backend was implemented in Flask (a python web framework).
The (very simple) frontend was implemented with AngularJS.
For the database layer mongodb was used.

The web server and db were containerized.

For the orchestration of the deployment docker-compose was used.

You can install docker-compose with the following command:

```shell
$ pip install docker-compose
```

For other methods refer to the official documentation.



Deploy
------
```shell
$ docker-compose up
```
or if you want everything to run in the background
```shell
$ docker-compose up -d
```

Prepare the database
--------------------
Execute the commands below inside the top directory of the cloned repository.

```shell
$ tr ";" "\t" < misc/spitogatos.csv  | docker exec -i housecat_db_1 mongoimport --type tsv --headerline --collection properties --db mydb
$ docker cp misc/transform.js housecat_db_1:/
$ docker exec housecat_db_1 mongo transform.js
```

Open http://localhost:5000/ in your browser.

Test
----
To run the tests:

```shell
$ docker-compose exec web tox
```

The tox command executes the unittests and flake8 for static analysis.
Also a coverage report is produced in the stdout.

Logs
----

View the logs

```shell
$ docker-compose logs web
$ docker-compose logs db
```
