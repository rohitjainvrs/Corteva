from src import app
from src.models.models import WeatherData, WeatherStatsData
from src.schema.schema import WeatherSchema, WeatherStatSchema
from flask import request, jsonify
from flasgger import Swagger

swagger = Swagger(app)


weather_schema = WeatherSchema(many=True)
weather_stat_schema = WeatherStatSchema(many=True)


@app.route("/weather", methods=["GET"])
def get_weather():
    """
    This endpoint returns a paginated list of weather data for a given date and station id,
    or for all weather data if no date or station id is specified.
    ---
    parameters:
        - name: page
          in: query
          type: integer
          default: 1
          description: The page number to return.
        - name: per_page
          in: query
          type: integer
          default: 100
          description: The number of results per page.
        - name: date
          in: query
          type: integer
          description: The date for which to return weather data (in YYYYMMDD format).
        - name: stationid
          in: query
          type: string
          description: The station id for which to return weather data.

    responses:
        200:
            description: OK
    """

    try:
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=100, type=int)
        date = request.args.get("date", type=int)
        stationid = request.args.get("stationid")

        query = WeatherData.query
        if date:
            query = query.filter_by(Dt=date)
        if stationid:
            query = query.filter_by(StationID=stationid)

        all_items = query.paginate(page=page, per_page=per_page, error_out=False)
        result = weather_schema.dump(all_items.items)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/weather/stats", methods=["GET"])
def get_stats():
    """
    This endpoint retrieves weather statistics based on the given parameters.
    ---
    parameters:
        - name: page
          in: query
          type: integer
          default: 1
          required: false
          description: The page number to return
        - name: per_page
          in: query
          type: integer
          default: 100
          required: false
          description: The number of items to return per page
        - name: year
          in: query
          type: integer
          required: false
          description: The year to filter by
        - name: stationid
          in: query
          type: string
          description: The station id for which to return weather data.
    responses:
        200:
            description: OK
    """
    try:
        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=100, type=int)
        year = request.args.get("year", type=int)
        stationid = request.args.get("stationid")

        query = WeatherStatsData.query
        if year:
            query = query.filter_by(Year=year)
        if stationid:
            query = query.filter_by(StationID=stationid)

        all_items = query.paginate(page=page, per_page=per_page, error_out=False)
        result = weather_stat_schema.dump(all_items.items)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
