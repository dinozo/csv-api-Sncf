import requests
import json
import pandas
import pprint


class Sncf:
    def __init__(self):
        self.json_obj = ""
        self.stops = ""
        self.headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}

    def read_json(self, url):
        try:
            req = requests.get(url)
            self.json_obj = json.loads(req.text)
            with open("stop_areas.JSON", mode="w+", encoding='utf-8') as data:
                json.dump(self.json_obj, data, sort_keys=True, indent=4, ensure_ascii=False)
            print("Json read")
        except FileNotFoundError:
            print("Error trying to read stop_area.JSON0")
            raise
        except ConnectionError:
            print("Url not valid, not found or user not connected to the internet")
            raise
        # return pprint.pprint(self.json_obj)

    def display_stops(self):
        new_data = []
        for areas in self.json_obj['stop_areas']:
            dicto = {
                'id': areas["id"],
                'codes-type': [codes["type"] for codes in areas["codes"]],
                'codes-value': [codes["value"] for codes in areas["codes"]],
                'Latitude': areas["coord"]["lat"],
                'Longitude': areas["coord"]["lon"],
                'label': areas["label"],
                'links': areas["links"],
                'name': areas["name"],
                'timezone': areas["timezone"],
            }
            if 'administrative_regions' in areas:
                dicto["Admin Regions"] = [regions['name'] for regions in areas['administrative_regions']]
            else:
                dicto["Admin Regions"] = "No regions"
            new_data.append(dicto)
        self.stops = new_data
        return new_data

    def insert_stop(self):
        pass

    def create_csv(self, data: object, fichier: str) -> object:
        info = pandas.DataFrame(data)
        f_name = fichier + ".csv"
        info.to_csv("csv/" + f_name)
        return info

    def format_datetime(self, datetime):
        for depart in datetime:
            formatted = {
                'year': depart[:4],
                'month': depart[4:6],
                'day': depart[6:8],
                'hour': depart[9:11],
                'minutes': depart[11:13],
                'seconds': depart[13:15]
            }
        return formatted

    def get_journey(self, start, stop):
        url = f"https://api.sncf.com/v1/journeys?from={start}&to={stop}"
        req = requests.get(url, headers=self.headers)
        raw_data = req.json()

        for data in raw_data['journeys']:
            my_stops = []
            my_departs = []
            my_arrivals = []
            # Get the sections from Journeys...
            section = data['sections']
            stops = len(section)
            print(f"There are {stops} stops")
            for sec in section:
                if "stop_date_times" in sec:
                    for stop in sec["stop_date_times"]:
                        arret = stop["stop_point"]["label"]
                        my_stops.append(arret)
                        if stop['base_departure_date_time'] and stop['arrival_date_time']:
                            arrival = stop['arrival_date_time']
                            departure = stop['base_departure_date_time']
                            my_arrivals.append(arrival)
                            my_departs.append(departure)
        # format date time

        my_new_data = {"Stops": my_stops, "departure time": my_departs, "arrival time": my_arrivals}
        df = pandas.DataFrame(my_new_data)
        print(df)
        # df.to_csv("journey/journey.csv")
