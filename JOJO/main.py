import requests
import json
URL = "https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/txt/3fa48b7d-ce01-4268-8cbf-a3eecc8df7bb.txt"
req = requests.get(URL)

def manip_json(req):
    raw_data = json.loads(req.text)
    my_json = json.dumps(raw_data,  sort_keys=True, indent=4)

    with open("stop_areas.JSON",mode="w") as data:
        data.write(my_json)
    print(my_json)

#manip_json(URL)

def insert_stop(file):
    dict_data = json.loads(req.text)
    print(dict_data)
    return dict_data


insert_stop("stop_areas.JSON")