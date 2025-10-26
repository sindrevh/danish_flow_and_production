import requests
import json

def retrive_right_now():
    """
    retrive_right_now(), pull latest data.
    """
    response = requests.get(
        url='https://api.energidataservice.dk/dataset/PowerSystemRightNow?limit=5')

    result = response.json()
    
    for k, v in result.items():
        print(k, v)

    records = result.get('records', [])

    print('records:')
    for record in records:
        print(' ', record)

    return result

def save_json_file(result, output_path):
    # Save json response as output.json file
    with open(output_path, 'w') as f:
        f.write(json.dumps(result, indent=4))