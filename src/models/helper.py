from ..data_processing.ingest import ingest_data, WeatherResult
from datetime import datetime


def init_data_process():
    print(f"Data Processing started at {datetime.now()}")
    data = ingest_data("../wx_data")
    result = WeatherResult(data)
    print(f"Data Processing Complete {datetime.now()}")
    return data, result
