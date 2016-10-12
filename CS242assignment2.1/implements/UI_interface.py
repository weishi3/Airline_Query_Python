__author__ = 'shiwei'
import webbrowser

from implements import Shortest_route, MyParser, Query, AboutRoute, Edit





#initial view

"""
parse the initial document and deal with user's operation in the first view
"""
def main():
    print("CSAir Query System")
    print("edited by Wei Shi")
    print("loading...")

    ui_parser = MyParser.MyParser("myData.txt")
    ui_parser.parse("init")

    print("Start Search Now\n")

    while True:
        display_menu()
        user_input = raw_input()
        if user_input == "1":
            query(ui_parser.code_indexed_cityList, ui_parser.searchForCode)
        elif user_input == "2" :
            print("If the system fails to open a chrome, open a browser and visit:")
            print(openMap(ui_parser.code_indexed_cityList, ui_parser.searchForCode))
        elif user_input == "q" :
            break
        elif user_input == "3":
            edit_operation(ui_parser.code_indexed_cityList, ui_parser.searchForCode)
        elif user_input == "4":
            AboutRoute.routeInformation(ui_parser.code_indexed_cityList, ui_parser.searchForCode)
        elif user_input == "5":
            file_name = raw_input("Source File: ")
            ui_parser.parse(file_name)
            print("Done. Data parsed in.")
        elif user_input == "6":
            file_name = raw_input("Name a new File: ")
            ui_parser.save_disk(file_name)
            print("Saved!")
        elif user_input == "7":
            Shortest_route.findShortestRoute(ui_parser.code_indexed_cityList, ui_parser.searchForCode)
        else:
            print("Invalid Input, try again!")

"""
deal with user's operation in the edit selection view
"""
def edit_operation(city_list, searchForCode):
    query = Query.Query(city_list, searchForCode)
    while(True):
        print("City List:")
        print_cities(query.get_all_city())
        valid_city = False
        while(not valid_city):
            print("Select a city to edit or q to go back:")
            city_name = raw_input()
            valid_city = city_name in searchForCode
            if(city_name == "q"):
                return 
            
        city = city_list[searchForCode[city_name]]
        
        
        while(True):
            print_edit_menu()
            user_input = raw_input()
            if(user_input == "1"):
                Edit.remove_city(city.name, city_list, searchForCode)
                print(city.name + " removed!")
                # special case to break since no more actions can occur on this list
                break
            elif(user_input =="2"):
                output = ""
                for destination in city.accessibleList:
                    output += destination + ", "
                print("valid destination to remove :"+output[:-2])
                
                valid_destination = False
                while(not valid_destination):
                    print("Select a Destination for removal")
                    destination = raw_input()
                    valid_destination = destination in city.accessibleList
                
                Edit.remove_route(city, destination)
                print("Route Removed!")
            elif(user_input =="3"):
                destination = raw_input("Destination Code: ")
                distance = int(raw_input("Distance: "))
                Edit.add_route(city, destination, distance)
                print("Route Added")
            elif(user_input =="4"):
                country = raw_input("New Country: ")
                Edit.change_country(city, country)
                print("Changed Country!")
            elif(user_input =="5"):
                continent = raw_input("New Continent Value: ")
                Edit.change_continent(city, continent)
                print("Changed Continent!")
            elif(user_input =="6"):
                timezone = int(raw_input("New Timezone Value: "))
                Edit.change_timezone(city, timezone)
                print("Changed Timezone!")
            elif(user_input == "7"):
                region = int(raw_input("New Region Value: "))
                Edit.change_region(city, region)
                print("Changed Region!")
            elif(user_input == "8"):
                population = int(raw_input("New Population Value: "))
                Edit.change_population(city, population)
                print("Changed Population!")
            elif(user_input == "9"):
                a=raw_input()
                b=raw_input()
                c=raw_input()
                d=raw_input()
                e=raw_input()
                f=raw_input()
                g=raw_input()
                h=raw_input()
                i=raw_input()

                Edit.add_city(a,b,c,d,e,f,g,h,city_list,searchForCode,i)
            elif(user_input == "q"):
                break
            else:
                print("Invalid input, try again...")


"""
print the guidance for edit
"""
def print_edit_menu():
    print("What do you want to modify? quit by 'q' :")
    print("1 - Remove City")
    print("2 - Remove a Route")
    print("3 - Add a Route")
    print("4 - Modify Country")
    print("5 - Modify Continent")
    print("6 - Modify Timezone")
    print("7 - Modify Region")
    print("8 - Modify Population")


# the view for choosing city

"""
deal with query on general infomation
"""
def query(city_list, searchForCode):
    the_query = Query.Query(city_list, searchForCode)

    while True:
        print("City List:")
        print_cities(the_query.get_all_city())
       # for i in the_query.get_all_city():
        #    print i,
        print
        print("Type a city for querying on or q to go back, Otherwise:")
        display_half()
        user_input = raw_input()
        if user_input == "q":
            return
        elif(user_input == "a"):
            print("From:    "+the_query.get_longest_flight()[0])
            print("To:      "+the_query.get_longest_flight()[1])
            print("Distance:"+str(the_query.get_longest_flight()[2]))
        elif(user_input =="b"):
            print("From:    "+the_query.get_shortest_flight()[0])
            print("To:      "+the_query.get_shortest_flight()[1])
            print("Distance:"+str(the_query.get_shortest_flight()[2]))
        elif(user_input =="c"):
            print("Average_distance :"+str(the_query.get_average_distance()))
        elif(user_input =="d"):
            print("Biggest_city :"+the_query.get_biggest_city()[0])
            print("Population_max :"+str(the_query.get_biggest_city()[1]))
        elif(user_input =="e"):
            print("Smallest_city :"+the_query.get_smallest_city()[0])
            print("Population_min :"+str(the_query.get_smallest_city()[1]))
        elif(user_input =="f"):
            print("Average_population: "+str(the_query.get_average_size()))
        elif(user_input == "g"):
            temp=the_query.get_continent_list().items()
            for i in temp:
                print(i[0]+":")
                for j in i[1]:
                    print j,
                print
        elif(user_input == "h"):
            for i in the_query.get_hub_city():
                print(i)
        elif user_input not in the_query.get_all_city():
            print("Invalid Input, try again")
            #print("Select a city for querying or q to go back:")
            query(city_list, searchForCode)
            return
        else:
            print
            display_query_doc()
            query_option(the_query,user_input,city_list,searchForCode)
        print

'''
helper function to print a list of cities
'''
def print_cities(city_list):
    cap = 16
    count = 0
    line = ""

    for city in city_list:
        line += city + ", "
        count += 1
        if(count == cap):
            print(line)
            count = 0
            line = ""
    if line != "":
        print(line[:-2])


"""
deal with query on a city
"""
def query_option(the_query,city, city_list, searchForCode):
    while True:
        user_input = raw_input()
        if(user_input == "1"):
            print("City_code: "+the_query.get_city_code(city))
        elif(user_input == "2"):
            print("Country :"+the_query.get_country(city))
        elif(user_input == "3"):
            print("Continent :"+the_query.get_continent(city))
        elif(user_input == "4"):
            print("Timezone :"+str(the_query.get_timezone(city)))
        elif(user_input == "5"):
            print(the_query.get_coordinates(city).items()[0][0]+": "+str(the_query.get_coordinates(city).items()[0][1]))
            print(the_query.get_coordinates(city).items()[1][0]+": "+str(the_query.get_coordinates(city).items()[1][1]))
        elif(user_input == "6"):
            print("Population :"+str(the_query.get_population(city)))
        elif(user_input == "7"):
            print("Region: "+str(the_query.get_region(city)))
        elif(user_input == "8"):
            for i in the_query.get_accessible_list(city_list[searchForCode[city]]):
                print("To: "+i[0]+"    Distance: "+str(i[1]))
        elif(user_input == "q"):
            return
        else:
            print("Invalid Input, try again!")


# open the map in a chrome
def openMap(city_list, searchForCode):
    URL = "http://www.gcmap.com/mapui?P="
    for i in city_list:
        city = city_list[i]
        departure_code = city.code
        for destination_code in city.accessibleList.keys():
            URL += (departure_code + "-" + destination_code + ",+")

    webbrowser.open_new(URL)
    return URL
"""
display the instruction of query
"""
def display_query_doc():
    print("Please Select a choice or press q to quit:")
    print("1 - City Code")
    print("2 - Country the city belongs to ")
    print("3 - Continent the city belongs to ")
    print("4 - Timezone of the city")
    print("5 - Coordinates of the city")
    print("6 - Population of the city")
    print("7 - Region of the city")
    print("8 - Cities directly accessible from the given city")


"""
display the query option for general info
"""
def display_half():
    print("a - Longest Flight Length")
    print("b - Shortest Flight Length")
    print("c - Average Flight Length")
    print("d - Biggest City & Population")
    print("e - Smallest City & Population")
    print("f - Average Population Size")
    print("g - List Continents with Cities")
    print("h - List of Hub Cities")

"""
display the original menu
"""
def display_menu():
    print("Send 1 or 2 to make the choice or Send q to quit:")
    print("1 - Query")
    print("2 - Glance at the Route Map")
    print("3 - Edit the Network")
    print("4 - Info about a Route")
    print("5 - Parse a File and Add to the Network")
    print("6 - Save Network to a File")
    print("7 - shortest route search")



if __name__ == '__main__':
    main()