import sys, os
import time

# Get the path of current file and find parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
import setup

import data_service_api
import data_transform
import data_packaging
import convert_file_for_ML

def main():
    if __name__ == '__main__':
        print("RUNNING main() \n")
        for i in range(setup.n_minutes):        
            if setup.debug == True:
                result = data_service_api.load_json_file(setup.debug_output_path)
            else:
                result = data_service_api.retrive_right_now()

            if setup.save_file == True:
                output_path = setup.debug_output_path
                data_service_api.save_json_file(result, output_path)

            n_hors, first_hour = data_transform.map_relevant_UTCs(result)

            average_dict = data_transform.parse_records(result, n_hors, first_hour)

            data_packaging.package_average_dict(average_dict)
            print(f"Data packaged for {average_dict.get("FirstMinute")}, waiting 60 seconds for API to refresh")

            time.sleep(60)

    print("STARTING NORMALISING JSON DATA FOR ML")

    MLReeadyDF = convert_file_for_ML.noramlise_json_data()
    convert_file_for_ML.save_normalised_df(MLReeadyDF, r"C:\git\danish_flow_and_production\output\output_time_series_file.pkl" )

    #TODO, feed in or further process dataframe (split to tokens). Need further specification of usecase.

    print("FINALIZED")
    
main()