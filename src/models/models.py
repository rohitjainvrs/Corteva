from .. import app, db
from sqlalchemy import Column, String, Float, Integer
from datetime import datetime
from .helper import init_data_process as data_processor


class WeatherData(db.Model):
    __tablename__ = "WeatherData"
    Dt = Column(String, primary_key=True)
    MaxTemp = Column(Float)
    MinTemp = Column(Float)
    PPT = Column(Float)
    StationID = Column(String, primary_key=True)
    Year = Column(Integer)

    def __init__(self, Dt, MaxTemp, MinTemp, PPT, StationID, Year):
        self.Dt = Dt
        self.MaxTemp = MaxTemp
        self.MinTemp = MinTemp
        self.PPT = PPT
        self.StationID = StationID
        self.Year = Year


class WeatherStatsData(db.Model):
    __tablename__ = "WeatherStatsData"
    Year = Column(Integer, primary_key=True)
    StationID = Column(String, primary_key=True)
    AvgMaxTemp = Column(Float)
    AvgMinTemp = Column(Float)
    AccPPT = Column(Integer)

    def __init__(self, Year, StationID, AvgMaxTemp, AvgMinTemp, AccPPT):
        self.Year = Year
        self.StationID = StationID
        self.AvgMaxTemp = AvgMaxTemp
        self.AvgMinTemp = AvgMinTemp
        self.AccPPT = AccPPT


with app.app_context():
    db.create_all()

    d_result, r_result = data_processor()
    print(f"Database Migration Started {datetime.now()}")
    d_result.to_sql("WeatherData", con=db.engine, if_exists="replace", index=False)
    r_result.to_sql("WeatherStatsData", con=db.engine, if_exists="replace", index=False)
    print(f"Database Migration Complete {datetime.now()}")
