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
d = datetime.timedelta(seconds=0)
print(f"There are {d.days} days, {str(d)[0]} hours, {str(d)[2:4]} minutes, {str(d)[5:7]} seconds")

for data in raw_data['journeys']:
    my_stops = []
    my_departs = []
    my_arrivals = []
    section = data['sections']
    stops = len(section)
    print(f"There are {stops} stops")
    for sec in section:
        if "stop_date_times" in sec:
            for stop in sec["stop_date_times"]:
                arret = stop["stop_point"]["label"]
                my_stops.append(arret)
                print("----------------------------")
                if stop['base_departure_date_time'] and stop['arrival_date_time']:
                    arrival = stop['arrival_date_time']
                    departure = stop['base_departure_date_time']
                    my_arrivals.append(arrival)
                    my_departs.append(departure)

my_new_data = {"Stops": my_stops, "departure time": my_departs, "arrival time": my_arrivals}
df = panda.DataFrame(my_new_data)
print(df)
df.to_csv("journey/journey.csv")