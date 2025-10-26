from src import data_transform
from datetime import datetime

def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_map_relevant_UTCs():
    
    tempData = {
        "limit": 1,
        "records":[
            {
            "Minutes1UTC": "2025-10-26T16:08:00",
            "Minutes1DK": "2025-10-26T17:08:00",
            "CO2Emission": 133.889999,
            "ProductionGe100MW": 1.31,
            "ProductionLt100MW": 419.709991,
            "SolarPower": 0,
            "OffshoreWindPower": 1241.050049,
            "OnshoreWindPower": 784.130005,
            "Exchange_Sum": 2603.47998,
            "Exchange_DK1_DE": 2472.560059,
            "Exchange_DK1_NL": 195.039993,
            "Exchange_DK1_GB": -959.159973,
            "Exchange_DK1_NO": -410,
            "Exchange_DK1_SE": 265,
            "Exchange_DK1_DK2": -143.179993,
            "Exchange_DK2_DE": 836.059998,
            "Exchange_DK2_SE": 213.669998,
            "Exchange_Bornholm_SE": -9.69,
            "aFRR_ActivatedDK1": -11.55,
            "aFRR_ActivatedDK2": 76.660004
        }]
    }

    n_hours, first_hour = data_transform.map_relevant_UTCs(tempData)

    assert first_hour == datetime.strptime("2025-10-26T16:08:00" , "%Y-%m-%dT%H:%M:%S")
    assert n_hours == 1


