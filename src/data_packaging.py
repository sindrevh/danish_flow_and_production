import setup
import json
from os import path

#TODO STORING TIME SERIES IN RELEVANT FORMAT (parquet?, QuestDB, etc.)


def package_average_dict(average_dict):
    
    outDict = {}

    if not path.isfile(setup.output_time_series_file):
        with open(setup.output_time_series_file, 'w') as f:
            outDict[average_dict.get("FirstMinute")] = average_dict
            f.write(json.dumps(outDict, indent=4))

    try:
        with open(setup.output_time_series_file, 'r', encoding='utf-8') as f:
            #Load existing values from files
            outDict = json.load(f)
            #Update value for defined first minute and update Dict
            outDict[average_dict.get("FirstMinute")] = average_dict

    except Exception as e:
        print(f"ERROR: Failed to load dict from {setup.output_time_series_file}, {e}")

    try:
        #Store updated dict as JSON, with update value.
        with open(setup.output_time_series_file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(outDict, indent=4))
    except Exception as e:
        print(f"ERROR: Failed to write dict from {setup.output_time_series_file}, {e}")
