import requests
import json
import pandas
import pprint
import datetime

class Sncf:
    def __init__(self):
        self.json_obj = ""
        self.stops = ""
        self.headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
        self.links = []
        self.datetime_now = self.get_datetime()

    def read_json(self, url):
        try:
            req = requests.get(url)
            self.json_obj = json.loads(req.text)
            with open("Not_used_anymore/stop_areas.JSON", mode="w+", encoding='utf-8') as data:
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
        #         'year': depart[:4],
        #         'month': depart[4:6],
        #         'day': depart[6:8],
        #         'hour': depart[9:11],
        #         'minutes': depart[11:13],
        #         'seconds': depart[13:15]
        time = f"{datetime[9:11]}h{datetime[11:13]}:{datetime[13:15]}"
        return time

    def get_datetime(self):
        """ Outputs the current date and  hous into a format accepted by the api YYYYMMDDDTHHMMSS"""
        # Format date into YYYYMMDD
        d_date = str(datetime.datetime.now().date())
        split = d_date.split("-")
        f_date = "".join(split)

        # Format Hour into HHMMSS
        hour = datetime.datetime.now().time()
        split_h = str(hour)
        f_hour = split_h[:2]+split_h[3:5]+split_h[6:8]

        #Formatted
        f_datetime = f_date + "T" + f_hour
        return f_datetime


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
                        if stop['departure_date_time'] and stop['arrival_date_time']:
                            arrival = self.format_datetime(stop['arrival_date_time'])
                            departure = self.format_datetime(stop['departure_date_time'])
                            my_arrivals.append(arrival)
                            my_departs.append(departure)
        # format date time
        my_new_data = {"Stops": my_stops, "departure": my_departs, "arrival": my_arrivals}
        return my_new_data

    def get_trains_datetime(self, start:str, stop:str, from_time="", to_time=""):

        endpoint = f"https://api.sncf.com/v1/coverage/sncf/journeys?to={stop}&datetime_represents=departure&from={start}&datetime=20210125T180000"
        req = requests.get(endpoint, headers=self.headers)
        raw_data = req.json()
        print(raw_data['links'])
