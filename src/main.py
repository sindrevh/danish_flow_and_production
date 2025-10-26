import sys, os

# Get the path of current file and find parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

import data_service_api
import setup

def main():
    if __name__ == '__main__':
        # Add your code that should only be executed when the script is run directly
        result = data_service_api.retrive_right_now()

        if setup.debug == True:
            output_path = r"C:\git\danish_flow_and_production\tests\test_data\energidataservice_right_now.json"
            data_service_api.save_json_file(result, output_path)

main()