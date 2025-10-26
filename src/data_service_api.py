import requests
import json
import setup

def retrive_right_now():
    """
    retrive_right_now(), pull latest data.
    """
    response = requests.get(
        url= setup.data_query_link + r"/PowerSystemRightNow?limit=5")

    result = response.json()
    
    return result

def retrive_meta_dataset():
    """
    retrive_right_now(), pull latest data.
    """
    response = requests.get(
        url= setup.data_query_link)

    result = response.json()
    
    return result

def save_json_file(result, output_path):
    # Save json response as output.json file
    with open(output_path, 'w') as f:
        f.write(json.dumps(result, indent=4))