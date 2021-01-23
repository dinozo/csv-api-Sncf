import requests
import json
import pprint
import pandas

class Sncf:
    def __init__(self):
        self.json_obj = ""

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
        #return pprint.pprint(self.json_obj)


    def display_stops(self):
        new_data = []
        regions = []
        dicto = {}
        administrative_regions = []
        for areas in self.json_obj['stop_areas']:
            if 'administrative_regions' in areas:
                for admin_region in areas['administrative_regions']:
                    regions.append(admin_region['name'])
                dicto = {'administrative_regions': regions}
                regions = []
            else:
                dicto['administrative_regions'] = "No administrative regions"
            # for codes in areas["codes"]:
            #     codes["type"]
            #     codes["value"]
            # areas["coord"]["lat"]0
            # areas["coord"]["lon"]
            # areas["id"]
            # areas["label"]
            # areas["links"]
            # areas["name"]
            # areas["timezone"]
            new_data.append(dicto)


        print(new_data)