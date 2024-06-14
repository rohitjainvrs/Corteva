import os
import pandas as pd
from tqdm import tqdm


def ingest_data(dirpath):
    data = []

    # Iterate over files in the directory
    for filename in tqdm(
        [f for f in os.listdir(dirpath) if f.endswith(".txt")], ascii=True
    ):
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "r") as file:
            for line in file:
                row = line.strip().split()
                # Add additional columns: StationID and Year
                row.extend([filename[:11], row[0][:4]])
                data.append(row)

    # Create DataFrame and assign column names
    df = pd.DataFrame(
        data, columns=["dt", "MaxTemp", "MinTemp", "PPT", "StationID", "Year"]
    )

    # Convert appropriate columns to integers
    df[["MaxTemp", "MinTemp", "PPT"]] = df[["MaxTemp", "MinTemp", "PPT"]].astype(int)

    # Filter out rows with missing values
    df = df[(df["MaxTemp"] != -9999) & (df["MinTemp"] != -9999) & (df["PPT"] != -9999)]

    return df


def WeatherResult(df):
    return (
        df.groupby(["Year", "StationID"])
        .agg(
            AvgMaxTemp=("MaxTemp", "mean"),
            AvgMinTemp=("MinTemp", "mean"),
            AccPPT=("PPT", "sum"),
        )
        .reset_index()
    )
