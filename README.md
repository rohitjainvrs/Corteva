# Code Challenge Template

# Installation
>create virtual environment:
>for windows
```bash
py -3 -m venv venv
venv\scripts\activate
```
>for mac:
```bash
python3 -m venv venv
source ./venv/bin/activate
```

>Install the required packages:
```bash
pip install -r requirements.txt
```

>Make .env file inside src folder

```bash
SQLALCHEMY_DATABASE_URI=sqlite:///Weather.db
SQLALCHEMY_TRACK_MODIFICATIONS=False
FLASK_ENV=development
```

>Go inside src folder

```bash
cd src
```

## Usage

- Run the following command to create the database and populate it with data:

- Start the API server
```bash
 python -m flask run
```
- The API can now be accessed at `http://localhost:5000`

---

### Endpoints

#### Swagger <br>
 `http://localhost:5000/apidocs/`

#### Weather data
```
GET /weather
```
This endpoint returns a paginated list of weather records. You can filter the results by date and stationid using query parameters:
```
GET /weather?date=19850103&stationid=USC00257715
```

##### Weather Stats data
```
GET /weather/stats

```
This endpoint returns statistical information about the weather data. You can filter the results by date and station using query parameters, in the same way as the /weather/ endpoint.

### Example Request

``` bash
 curl -X GET "http://localhost:5000/weather?date=19850103&stationid=USC00257715"
```
### Example Response
```json
[
    {
        "date":"19850103",
        "maximum_temperature":22,
        "minimum_temperature":-111,
        "precipitation":0,
        "station":"USC00257715"
    }
]
```


# Testing

## Run the tests
### come out from src folder and go to tests folder
>cd ..

>cd tests

```bash
pytest -W ignore::DeprecationWarning
```