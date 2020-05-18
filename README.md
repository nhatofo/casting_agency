# Casting Agency

Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

Hosted on heroku. [Link](https://teocastingagency.herokuapp.com/).

## Motivation

This is my capstone project for the Udacity FSWD nanodegree.

## Dependencies

All dependencies are listed in the `requirements.txt` file. 
They can be installed by running `pip3 install -r requirements.txt`.

## Authentication

The API has three registered users with diferent roles:

1. Casting Assistant

###
email: assistant@fsnd.com
pass: Pass1231
###

2. Casting Director

###
email: director@fsnd.com
pass: Pass1232
###

3. Producer

###
email: producer@fsnd.com
password: Pass1233
###

## Api Endpoints

### `GET /movies`

Gets all movies from the database.

Response:

```json5
{
  "movies": [
    {
      "id": 1,
      "movies": "all acted movies here",
      "release_date": "2021-02-02",
      "title": "Movie"
    },
    {
      "id": 2,
      "movies": "all acted movies here",
      "release_date": "2019-01-01",
      "title": "New movie"
    }
  ],
  "success": true
}
```

### `POST /movies`

Adds a new movie to the database.

Data:

```json5
{
  "title": "title",
  "release_date": "release_date"
}
```

Response:

```json5
{
  'success': true,
  'movie': 'title'
}
```

### `PATCH /movies/<int:id>`

Edit data on a movie in the database.

Data:

```json5
{
  "title": "new title",
  "release_date": "2021-02-02"
}
```

Response:

```json5
{
  'success': true,
  'movie': {
              "id": 1,
              "movies": "all acted movies here",
              "release_date": "2021-02-02",
              "title": "new title"
            }
}
```

### `DELETE /movies/<int:id>`

Delete a movie from the db.

Response:

```json5
{
  'success': true,
  'delete': 1
}
```

### `GET /actors`

Gets all actors from the database.

Response:

```json5
{
  "actors": [
    {
      "gender": "M",
      "id": 1,
      "movies": "all acted movies here",
      "name": "actor"
    },
    {
      "gender": "F",
      "id": 2,
      "movies": "all acted movies here",
      "name": "ewwe"
    }
  ],
  "success": true
}
```

### `POST /actors`

Adds a new actor to the database.

Data:

```json5
{
  "name": "name",
  "gender": "F"
}
```

Response:

```json5
{
  'success': true,
  'actor': 'name'
}
```

### `PATCH /actors/<int:id>`

Edit data on a actor in the database.

Data:

```json5
{
  "name": "new name",
  "gender": "M"
}
```

Response:

```json5
{
  'success': true,
  'actor': {
              "gender": "M",
              "id": 1,
              "movies": "all acted movies here",
              "name": "new name"
            }
}
```

### `DELETE /actors/<int:id>`

Delete a actor from the database.

Response:

```json5
{
  'success': true,
  'delete': 1
}
```

### Prerequisites

postgress database instance and python 3.x installed on doker  or linux Ubuntu 14.04 or above with all above requirements librires installed.

### Installing
Use the etl.ipynd notebook to develop the ETL process for each of tables before completing running the  etl.py file to load the whole datasets.

Each time you run the cells above, remember to restart this notebook to close the connection to your database. Otherwise, you won't be able to run your code in create_tables.py, etl.py, or etl.ipynb files since you can't make multiple connections to the same database (in this case, sparkifydb).

### Running the tests
To run tests,just execute the python file  test_app.py.(python3 test_app.py)




### Built With

* [Postgress](https://www.postgresql.org/) - Database Management System
* [Python](https://www.python.org/) - Scripting Language
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web development framework

### Contributing
* **Teofilo Carlos Chichume ** 


### Authors

* **Teofilo Carlos Chichume** - *Initial work* - [nhatofo](https://github.com/nhatofo/udacity_de.git)


### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

* Inspiration [yuralim](https://github.com/yuralim/udacity_dend_project1),
[PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)