import requests
import json
import pandas as panda

HEADERS = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}

# with open("filtered.py", "w", encoding='utf-8') as file:
#     to_clean = json.dumps(raw_data, sort_keys=True, indent=4, ensure_ascii=False)
# file.write(to_clean)


def make_dataframe():
    url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
    req = requests.get(url, headers=HEADERS)
    raw_data = json.loads(req.text)

    new_data = []
    with open("stop_areas.JSON") as file:
        json_data = json.load(file)
        for data in json_data['stop_areas']:
            dicto = {
                "Stop name": data['name'],
                "Code": data['codes'][0]['type'],
                "Code value": data['codes'][0]['value'],
                "Latitude": data['coord']['lat'],
                "Longitude": data['coord']['lon'],
            }
            if 'administrative_regions' in data:
                dicto["Admin Regions"] = [regions['name'] for regions in data['administrative_regions']]
            else:
                dicto["Admin Regions"] = "No regions"

            new_data.append(dicto)

    info = panda.DataFrame(new_data)
    info.to_csv("stop_areas.csv")


