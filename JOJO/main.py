import requests
import json
from stop_areas import my_data_dict

URL = "https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/txt/3fa48b7d-ce01-4268-8cbf-a3eecc8df7bb.txt"
req = requests.get(URL)


def manip_json():
    raw_data = json.loads(req.text)
    my_json = json.dumps(raw_data, sort_keys=True, indent=4)
    with open("stop_areas.JSON", mode="w") as data:
        data.write(my_json)
    print(my_json)


# manip_json()

def insert_stop(key):
    # Creates stop_areas.py and construct a dictionary
    # my_dict = req.text
    # with open("stop_areas.py",mode="w") as data:
    #     data.write(my_dict)

    # Get the format of an stop area
    # (my_data_dict[key][0])
    print(my_data_dict[key][0].keys())


insert_stop('stop_areas')
