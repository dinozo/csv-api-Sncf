import requests
import json
from sncf import Sncf
import pprint

sncf = Sncf()
sncf.read_json("https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/txt/3fa48b7d-ce01-4268-8cbf-a3eecc8df7bb.txt")
sncf.display_stops()

'''
def insert_stop(key):
    # model the new data
    new_stop_area = {
        "administrative_regions": [
            {
                "coord": {
                    "lat": "50.23436",
                    "lon": "7.996379"
                },
                "id": "admin:1187560extern",
                "insee": "",
                "label": "Venezuela",
                "level": 15,
                "name": "Venezuela",
                "zip_code": "8001"
            },
            {
                "coord": {
                    "lat": "51.23436",
                    "lon": "8.996379"
                },
                "id": "admin:5432693extern",
                "insee": "",
                "label": "Bresil",
                "level": 10,
                "name": "Bresil",
                "zip_code": ""
            }
        ],
        "codes": [
            {
                "type": "VE-VB-BR",
                "value": "0080-300520-BV"
            }
        ],
        "coord": {
            "lat": "50.24065",
            "lon": "7.6990968"
        },
        "id": "stop_area:BRE:VE:90503914",
        "label": "VENEZUELA",
        "links": [],
        "name": "VENEZUELA-BR",
        "timezone": "Amerique/New-york"
    }
    with open("stop_areas.JSON", mode="r") as file:
        data = json.load(file)
        data['stop_areas'].insert(0, new_stop_area)
        manip_json(data)
        print("operation succeded")

    # Creates stop_areas.py and construct a dictionary
    # Get the format of an stop area, the first one
    # (my_data_dict[key][0])
    # print(my_data_dict[key][0].items())
    # STOP AREAS is a list of dictionaries of administrative regions
    # The keys are 'codes', 'name', 'links', 'coord', 'label', 'administrative_regions', 'timezone', 'id'
'''

# insert_stop('stop_areas')
