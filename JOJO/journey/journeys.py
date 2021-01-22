import requests
import json
import datetime
import pandas as panda
from JOJO.csvmanip import HEADERS

# From  Paris - Gare de Lyon
depart = "stop_area:OCE:SA:87686006"
# To Lyon - Perrache
arrival = "stop_area:OCE:SA:87722025"

# Request
URL = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrival}"
req = requests.get(URL, headers=HEADERS)

#Push the request to a JSON
#with open("journey/journey.JSON", "r+", encoding='utf-8') as file:
    #json.dump(req.json(), file, sort_keys=True, indent=4)

raw_data = req.json()
new_data = []
for data in raw_data['journeys']:
    section = data['sections']
    stops = len(section)
    print(f"There are {stops} stops")
    for sec in section:
        if "stop_date_times" in sec:
            stops = [new_data.append(stop["stop_point"]["label"]) for stop in sec["stop_date_times"]]

new_dict = {"Stops": new_data}

df = panda.DataFrame(new_dict)
print(df)