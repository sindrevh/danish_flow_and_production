import requests
import json
import setup

def retrive_right_now(limit = 5):
    """
    retrive_right_now(), pull latest data.
    """
    response = requests.get(
        url= setup.data_query_link + r"/PowerSystemRightNow?limit=" + str(limit))

    result = response.json()
    
    return result

def retrive_meta_dataset():
    """
    retrive_meta_dataset(), pull latest metadata.
    """
    response = requests.get(
        url= setup.data_query_link)

    result = response.json()
    
    return result

def save_json_file(result, output_path):
    # Save json response as output.json file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, indent=4))

def load_json_file(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        return json.load(f)