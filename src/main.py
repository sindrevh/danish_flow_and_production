import data_service_api

def main():
   if __name__ == '__main__':
       # Add your code that should only be executed when the script is run directly
       result = data_service_api.retrive_right_now()
       output_path = r"C:\Temp\energidataservice\energidataservice_right_now.json"
       data_service_api.save_json_file(result, output_path)

main()