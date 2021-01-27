from sncf import Sncf
import pandas
# Create an instance of the class Sncf
sncf = Sncf()

# Call the method read_json to do a get request to an determined api
# url = "https://simplonline-v3-prod.s3.eu-west-3.amazonaws.com/media/file/txt/3fa48b7d-ce01-4268-8cbf-a3eecc8df7bb.txt"
# broke_url = "https://simplonline-v3-prod.s3.eu-west-3.amazonawscom/media/file/txt/3fa48b7d-ce01-4268-8cbf-a3eecc8df7bb.txt"
# sncf.read_json(broke_url)

# Call the display stops method to display all stops, coordinates, codes,
# and administative regions and create an stops attribute
# stops = sncf.display_stops()

# Call the method create_csv to transfer the stops attribute from the last method into a CSV dataframe
# x = sncf.create_csv(stops, "stop_areas")
# print(x)

# Get the stops from Paris GARE DE LYON to Lyon Perrache

# From  Paris - Gare de Lyon
depart = "stop_area:OCE:SA:87686006"
# To Lyon - Perrache
arrival = "stop_area:OCE:SA:87722025"
# Call the metohod and will return the new data
# my_journey = sncf.get_journey(depart, arrival)
# pd = pandas.DataFrame(my_journey)
# print(pd)
# post the journey into a CSV
# sncf.create_csv(my_journey, "Journey")

# Get the trains from Paris to Lyon entre 18h et 20h
# date_only_today = sncf.date_only
# #18 heures in format HHMMSS
# hour_of_depart = "180000"
# sncf.get_trains_datetime(start=depart, stop=arrival, from_time=hour_of_depart)
# #
# sncf.get_all_journeys("https://api.navitia.io/v1/coverage/sncf/journeys?to=stop_area%3AOCE%3ASA%3A87722025&datetime_represents=departure&from=stop_area%3AOCE%3ASA%3A87686006&datetime=20210126T183001")
#
#
# Get all stop_areas
# sncf.get_all_stop_areas()

# get the stop areas to perpignan
query_area = sncf.search_stop_area("perpignan")

my_journey = sncf.get_journey(depart, query_area)

pd = pandas.DataFrame(my_journey)
print(pd)
# post the journey into a CSV
sncf.create_csv(my_journey, "Journey_to_perpignan")