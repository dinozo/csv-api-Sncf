import requests
import json
import pandas
import time
import pprint
import datetime
import os
import logging
import pathlib

logfile = pathlib.Path(f'{os.getcwd()}/logs/logs.log')
logging.basicConfig(filename=logfile, format='%(asctime)s: %(levelname)s: %(message)s', level=logging.DEBUG,
                    datefmt='[%Y-%m-%d %H:%M:%S]')
logging.info("Import of modules succeded")


class Sncf:
    def __init__(self):
        self.json_obj = None
        self.stops = None
        self.headers = {"Authorization": "0157b284-3cc3-4799-a1ab-79dc2761d274"}
        self.links = []
        self.datetime_now = self.get_date() + self.get_hour()
        self.date_only = self.get_date()
        self.options = {
            "0": "0 - to exit and shut down the program",
            "1": "1 - Call a method to read an API and save it into a  json file",
            "2": "2 - Insert an stop area into a json saved file",
            "3": "3 - Create a csv with all the gares / stop areas / codes etc. ",
            "4": "4 - Read a CSV and print it in an organized dataframe ",
            "5": "5 - Obtain the information for a Sample trajet, ex. Paris - Lyon",
            "6": "6 - Check the trains between paris gare de lyon and lyon perrache between a defined interval of hours",
            "7": "7 - Get the trains from paris et perpignan!",
            "8": "8 - Get the trains from  paris to your own query destination",
            "9": "9 - Get the trains from your destination to your own another destination"
        }

    def read_json_api(self, url, name="dump", mode="w+"):
        try:
            req = requests.get(url, headers=self.headers)
            json_object = json.loads(req.text)
            filename = "json/" + name + ".JSON"
            with open(filename, mode=mode, encoding='utf-8') as data:
                json.dump(json_object, data, sort_keys=True, indent=4, ensure_ascii=False)
            return json_object
        except FileNotFoundError:
            print("Error trying to read file.JSON")
        except requests.exceptions.ConnectionError:
            print("Url not valid, not found or user not connected to the internet")

    def pprint_json(self, url):
        req = requests.get(url, headers=self.headers)
        obj = req.json()
        pprint.pprint(obj)

    def read_local_json(self, filename):
        with open(f"json/{filename}.json", mode="r", encoding='utf-8') as file:
            local = json.load(file)
        return local

    def display_stops(self, json_obj):
        new_data = []
        for areas in json_obj['stop_areas']:
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

    def display_all_stops(self, json_obj):
        new_data = []
        for objeto in json_obj:
            for areas in objeto['stop_areas']:
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
                    dicto["admin-regions"] = [regions['name'] for regions in areas['administrative_regions']]
                else:
                    dicto["admin-regions"] = "No regions"
                new_data.append(dicto)
            self.stops = new_data
        return new_data

    def insert_stop(self):
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

        pass

    @staticmethod
    def create_csv(data: dict, fichier: str) -> object:
        info = pandas.DataFrame(data)
        f_name = fichier + ".csv"
        info.to_csv("csv/" + f_name)
        return info

    @staticmethod
    def read_csv(csv_file):
        result = pandas.read_csv(f"csv/{csv_file}.csv")
        print(result)
        return result

    @staticmethod
    def my_duration(seconds):
        a = str(datetime.timedelta(seconds=seconds))[0:7]
        return a

    @staticmethod
    def format_datetime(my_datetime):
        #         'year': depart[:4],
        #         'month': depart[4:6],
        #         'day': depart[6:8],
        #         'hour': depart[9:11],
        #         'minutes': depart[11:13],
        #         'seconds': depart[13:15]
        my_time = f"{my_datetime[9:11]}h{my_datetime[11:13]}"
        return my_time

    @staticmethod
    def get_date(date=datetime.datetime.now().date()):
        d_date = str(date)
        split = d_date.split("-")
        f_date = "".join(split)
        return f_date + "T"

    @staticmethod
    def get_hour(hour=datetime.datetime.now().time()):
        # Format Hour into HHMMSS
        split_h = str(hour)
        f_hour = split_h[:2] + split_h[3:5] + split_h[6:8]
        return f_hour

    @staticmethod
    def get_attente(arrival, depart):
        # process arrival 
        a = datetime.datetime.strptime(arrival, "%Hh%M")
        d = datetime.datetime.strptime(depart, "%Hh%M")
        diff = (d - a).total_seconds()
        attente = time.strftime("%Mmin", time.gmtime(diff))
        return attente

    def get_journey(self, start, stop, link=""):
        if link == "":
            link = f"https://api.sncf.com/v1/journeys?from={start}&to={stop}"
        req = requests.get(link, headers=self.headers)
        raw_data = req.json()

        for data in raw_data['journeys']:
            my_stops = []
            my_departs = []
            my_arrivals = []
            my_attente = []
            # Get the sections from Journeys...
            section = data['sections']
            for sec in section:
                if "stop_date_times" in sec:
                    for stop in sec["stop_date_times"]:
                        arret = stop["stop_point"]["label"]
                        my_stops.append(arret)
                        if stop['departure_date_time'] and stop['arrival_date_time']:
                            arrival = self.format_datetime(stop['arrival_date_time'])
                            departure = self.format_datetime(stop['departure_date_time'])
                            attente = self.get_attente(arrival=arrival, depart=departure)
                            my_arrivals.append(arrival)
                            my_departs.append(departure)
                            my_attente.append(attente)
        # format date time
        print(f"There are {len(my_stops) - 1} stops")

        my_new_data = {"Stops": my_stops,
                       "arrival": my_arrivals,
                       "departure": my_departs,
                       "attente": my_attente}
        return my_new_data

    def get_all_journeys(self, api):
        raw_data = self.read_json_api(api)
        my_section_list = []
        for journey in raw_data['journeys']:
            # ----- now divide and treat each section.
            for count, section in enumerate(journey['sections']):
                if section['type'] != 'crow_fly':
                    my_section = {
                        'Section': count,
                        'id': section['type'],
                        'departure': self.format_datetime(section['departure_date_time']),
                        'arrival': self.format_datetime(section['arrival_date_time']),
                        'duration': self.my_duration(section['duration'])

                    }
                    if "from" and "to" in section:
                        my_section['from'] = section['from']['name']
                        my_section['to'] = section['to']['name']
                    else:
                        my_section["from"] = section['type']
                        my_section["to"] = section['type']
                    my_section["type"] = journey['type']
                    my_section["transfers"] = journey['nb_transfers']
                    my_section["duration"] = self.my_duration(journey['duration'])
                    my_section_list.append(my_section)
            # ----  end of section
            break
        return my_section_list

    def get_trains_datetime(self, start: str, stop: str,
                            from_time: str, to_time: str):
        datetime_query = self.get_date() + from_time
        endpoint = f"https://api.sncf.com/v1/coverage/sncf/journeys?to={stop}" \
                   f"&datetime_represents=departure&from={start}&datetime={datetime_query}"
        raw_data = self.read_json_api(endpoint, name="trains-datetime")
        links = [i['href'] for i in raw_data['links']]
        #loop many times and change the time to get the first 2 trajets every hour..
        all_data = []
        for link in links:
            try:
                datetime_query = int(link[-6::])
                if int(from_time) < datetime_query < int(to_time):
                    # FIX, the query is good, the function get_journey is NOT
                    data = self.get_all_journeys(api=link)
                    all_data.extend(data)
            except ValueError:
                pass
        df = pandas.DataFrame(data for data in all_data)
        pprint.pprint(df)
        return df

    def get_all_stop_areas(self):
        num = 1
        if os.path.isfile("json/all_stop_areas.JSON"):
            print("All stop areas JSON already exist")
            if os.path.isfile("csv/all_stop_areas.csv"):
                print("All stop areas csv already exist")
            else:
                with open("json/all_stop_areas.JSON") as file:
                    raw_data = json.load(file)
                new_data = self.display_all_stops(raw_data)
                df = pandas.DataFrame(new_data)
                df.to_csv("csv/all_stop_areas.csv")
        else:
            all_request = []
            for i in range(1, 5):
                api_url = "https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000&start_page=" + str(i)
                req = requests.get(api_url, headers=self.headers)
                all_request.append(req.json())
            filename = "json/all_stop_areas.JSON"
            with open(filename, mode="a", encoding='utf-8') as data:
                json.dump(all_request, data, sort_keys=True, indent=4, ensure_ascii=False)

    def search_stop_area(self, gare):
        read = pandas.read_csv("csv/all_stop_areas.csv")
        try:
            query = read[read["name"] == gare.capitalize()]
            return query['id'].values[0]
        except IndexError:
            print(gare + " DOESNT EXIST! try to look for it in all_stop_areas.csv")
