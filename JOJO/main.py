from sncf import Sncf
import pandas
import matplotlib.pyplot as plt
import os

# Create an instance of the class Sncf
sncf = Sncf()

def main():
    app_on = True
    print("Welcome to the API SNCF By Jojo! in this api you can do some things")

    for items in sncf.options.values():
        print(items)
    # The main input
    master = input("What do you want to do? , type a number: ")

    # Shut down
    if master == "0":
        app_on = False

    # Call the method read_json to do a get request to an determined api
    if master == "1":
        use = input("Do you want to use your own URL or use the default one, type: 'use' or 'def' :")
        if use.lower() == "def":
            url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        else:
            url = input("paste your api url here: ")
        sncf.pprint_json(url)
        name_file = input("Press write the 'name' of the file to save  it, otherwise press Enter")
        if name_file != "":
            sncf.read_json_api(url, name_file)
            print(f"Saved into json folder as {name_file}.JSON")

    # Add un arret dans le JSON
    if master == "2":
        "This function is not ready yet"
        pass

    # Create a csv with all the gares / stop areas / codes etc.
    if master == "3":
        # Read the stop_areas.JSON
        jsons = os.listdir("./json")
        print(jsons)
        name = input("Whats the name of the file.json to read? ex. stop_areas: ")
        my_json = sncf.read_local_json(name)
        data = sncf.display_stops(my_json)
        csv_name = input("how would you name your csv?: ")
        sncf.create_csv(data, csv_name)
        print(f"Your csv is in  csv/{csv_name}.csv")

    # Read a CSV and print a organized dataframe
    if master == "4":
        x = os.listdir("./csv")
        print(x)
        csv_file = input("Wich of the listed csv files would you like to print into a Dataframe?, write only the name")
        sncf.read_csv(csv_file)

    # From  Paris - Gare de Lyon
    depart = "stop_area:OCE:SA:87686006"
    # To Lyon - Perrache
    arrival = "stop_area:OCE:SA:87722025"

    # Obtain the information for a Sample trajet, ex. Paris - Lyon""
    if master == "5":
        # Call the method and will return the new data
        my_journey = sncf.get_journey(depart, arrival)
        pd = pandas.DataFrame(my_journey)
        print(pd)
        # post the journey into a CSV
        save = input("Do you want to save it ? input your file name, otherwise press Enter: ")
        if save != "":
            sncf.create_csv(my_journey, save)
            print(f"Your csv is in  csv/{save}.csv")

    # Check the trains between paris gare de lyon and lyon perrache between a defined interval of hours!
    if master == "6":
        # hours in format HHMMSS
        hour_of_depart = input("What is the EARLIEST time you would like to travel? (24 hours) in format HHMM: ") + "00"
        max_hour_of_depart = input(
            "What is the LATEST time you would like to travel? (24 hours) in format HHMM: ") + "00"
        if max_hour_of_depart < hour_of_depart:
            print("latest hour cannot be less than the earliest hour")
        query = sncf.get_trains_datetime(start=depart, stop=arrival, from_time=hour_of_depart,
                                         to_time=max_hour_of_depart)
        save = input("Do you want to save this in csv ? input your file name, if NOT press Enter: ")
        if save != "":
            sncf.create_csv(query, save)
            print(f"Your csv is in  csv/{save}.csv")

    # Get the trains from paris et perpignan!
    if master == "7":
        # Get all stop_areas
        sncf.get_all_stop_areas()

        query_area = sncf.search_stop_area("perpignan")
        my_journey = sncf.get_journey(depart, query_area)
        pd = pandas.DataFrame(my_journey)
        print(pd)

        # this code needs to have his own function
        # post the journey into a CSV
        save = input("Do you want to save this in csv ? input your file name, if NOT press Enter: ")
        if save != "":
            sncf.create_csv(my_journey, save)
            print(f"Your csv is in  csv/{save}.csv")

    # Get the trains from  paris to your own query destination
    if master == "8":
        # Get all stop_areas
        sncf.get_all_stop_areas()
        gare = input("Supposing that you are in paris gare de lyon, where do you want to go?: ")
        query_area = sncf.search_stop_area(gare)
        print(query_area)
        my_journey = sncf.get_journey(depart, query_area)
        pd = pandas.DataFrame(my_journey)
        print(pd)

        # post the journey into a CSV
        save = input("Do you want to save this in csv ? input your file name, if NOT press Enter: ")
        if save != "":
            sncf.create_csv(my_journey, save)
            print(f"Your csv is in  csv/{save}.csv")

    # Get the trains from your destination to your own another destination
    if master == "9":
        # From  Paris - Gare de Lyon
        gare = input("Where are you?: ")
        depart = sncf.search_stop_area(gare)
        # To Lyon - Perrache
        gare2 = input("where do you want to go?: ")
        arrival = sncf.search_stop_area(gare2)

        my_journey = sncf.get_journey(depart, arrival)
        pd = pandas.DataFrame(my_journey)
        print(pd)
        # post the journey into a CSV
        save = input("Do you want to save it ? input your file name, otherwise press Enter: ")
        if save != "":
            sncf.create_csv(my_journey, save)
            print(f"Your csv is in  csv/{save}.csv")

    # Show the graphic gares atteintes en un seul trajet et celles atteintes avec une correspondance.
    if master == "10":
        # hours in format HHMMSS
        #gare_depart = input("")
        #plot_depart = sncf.search_stop_area(gare)
        #print(query_area)

        hour_of_depart = "070000"
        max_hour_of_depart = "235900"
        query = sncf.get_trains_datetime(start=depart, stop=arrival, from_time=hour_of_depart,
                                         to_time=max_hour_of_depart)

        graph = query.plot.scatter(x="from", y="transfers",  s=50)
        plt.savefig("mygraph.png")


if __name__ == "__main__":
    main()
