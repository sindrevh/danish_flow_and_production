from datetime import datetime

def map_relevant_UTCs(json_result):
    numer_of_hours : int = int(json_result.get('limit'))

    list_of_records = json_result.get('records')

    if len(list_of_records) == 0:
        return (0, None)

    first_hour = datetime.strptime(list_of_records[len(list_of_records)-1].get("Minutes1UTC"), "%Y-%m-%dT%H:%M:%S")
    #last_hour = list_of_records[0].get("Minutes1UTC")

    return (numer_of_hours, first_hour)

def parse_records(json_result, n_minutes, first_minute):

    average_dict = {}

    average_dict["FirstMinute"] = first_minute.strftime('%Y-%m-%dT%H:%M:%S')
    average_dict["nMinutes"] = n_minutes

    for record in json_result.get('records'):
        for key in record.keys():
            temp_value = record.get(key)
            if type(temp_value) == float:

                temp_value = temp_value / n_minutes #To account for avveraging per n_hour

                if average_dict.get(key) == None:
                    average_dict[key] = temp_value
                else:
                    average_dict[key] = temp_value + average_dict[key]
                    
    return average_dict
