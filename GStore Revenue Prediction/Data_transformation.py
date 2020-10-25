import numpy as np
import pandas as pd
import json
import os
from pandas.io.json import json_normalize



# transfer Jason format to column

def load_df(csv_path='kaggle/train.csv', nrows=None):
    JSON_COLUMNS = ['device', 'geoNetwork', 'totals', 'trafficSource']
    df = pd.read_csv(csv_path,converters={column: json.loads for column in JSON_COLUMNS},dtype={'fullVisitorId': 'str'},nrows=nrows)
    for column in JSON_COLUMNS:
        column_as_df = json_normalize(df[column])
        column_as_df.columns = [f"{column}.{subcolumn}" for subcolumn in column_as_df.columns]
        df = df.drop(column, axis=1).merge(column_as_df, right_index=True, left_index=True)
    print(f"Loaded {os.path.basename(csv_path)}. Shape: {df.shape}")
    return df
