from .. import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class WeatherSchema(ma.Schema):
    class Meta:
        fields = ("Dt", "MaxTemp", "MinTemp", "PPT", "StationID", "Year")


class WeatherStatSchema(ma.Schema):
    class Meta:
        fields = ("Year", "StationID", "AvgMaxTemp", "AvgMinTemp", "AccPPT")
