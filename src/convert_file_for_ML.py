import json
import pandas as pd
import os

import setup

def noramlise_json_data():
    try:
        with open(setup.output_time_series_file, 'r') as f:
            data = json.load(f)
            
            df = pd.json_normalize(data)
            print(f"output_time_series_file normalised and returned as dataframe")
            
            return df

    except Exception as e:
        print(f"Failed to load output_time_series_file, {e}")
        return None
    
def save_normalized_df(df, file_path):
    df.to_pickle(file_path)

def load_normalized_df(file_path):
    if os.path.isfile(file_path):
        return pd.read_pickle(file_path)
    else:
        print(f"ERROR: Failed to load normalised data frame from {file_path}")