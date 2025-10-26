import json
from pandas import json_normalize

import setup

def noramlise_json_data():
    try:
        with open(setup.output_time_series_file, 'r') as f:
            data = json.load(f)
            
            df = json_normalize(data)
            print(f"output_time_series_file normalised and returned as dataframe")
            
            return df

    except Exception as e:
        print(f"Failed to load output_time_series_file, {e}")
        return None