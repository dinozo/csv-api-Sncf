from sncf import Sncf
import pandas
import pprint

# Create an instance of the class Sncf
sncf = Sncf()


def main():
    print("Welcome to the API SNCF! in this api you can do some things")

    options =  {
        "1": "1 - Call a method to read an API and save it into a  json file",
        "2": "2 - Make pasta"
    }
    for items in options.values():
        print(items)
    # The main input
    master = input("What do you want to do? , type a number: ")

    # Call the method read_json to do a get request to an determined api
    if master == "1":
        use = input("Do you want to use your own URL or use the default one, type: 'use' or 'def' :")
        if use.lower() == "def":
            url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        else:
            url = input("paste your api url here: ")
        sncf.pprint_json(url)
        if input("Press write 's' to SAVE  it") == "s":
            sncf.read_json(url)
            print("Saved into json as dump.JSON")

    # Add un arret dans le JSON
    if master == "2":
        pass

    if master == "3":
        pass

    # Call the display stops method to display all stops, coordinates, codes,
    # and administative regions and create an stops attribute
    # stops = sncf.display_stops()

    # Call the method create_csv to transfer the stops attribute from the last method into a CSV dataframe
    # x = sncf.create_csv(stops, "stop_areas")
    # print(x)

    # Get the stops from Paris GARE DE LYON to Lyon Perrache

    # From  Paris - Gare de Lyon
    # depart = "stop_area:OCE:SA:87686006"
    # To Lyon - Perrache
    #arrival = "stop_area:OCE:SA:87722025"
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
    # query_area = sncf.search_stop_area("perpignan")
    #
    # my_journey = sncf.get_journey(depart, query_area)
    #
    # pd = pandas.DataFrame(my_journey)
    # print(pd)
    # # post the journey into a CSV
    # sncf.create_csv(my_journey, "Journey_to_perpignan")

if __name__ == "__main__":
    main()
