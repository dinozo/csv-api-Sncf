import unittest
from sncf import Sncf
import random
import os
sncf = Sncf()
name_list = ["a", "b", "c"]
URL = "https://api.navitia.io/v1/coverage/sncf/journeys?from=stop_area%3AOCE%3ASA%3A87722025"
BROKE_URL = "https://api.navitiaio/v1/coverage/sncf/journeys?from=stop_area%3AOCE%3ASA%3A87722025"

class testSNCF(unittest.TestCase):

    def test_read_json(self):
        random.shuffle(name_list)
        name = "".join(name_list)
        self.assertTrue(sncf.read_json_api(url=URL, name=name), os.path.isfile(f"json/{name}.JSON"))
        os.remove(f"json/{name}.JSON")


if __name__ == '__main__':
    unittest.main()
