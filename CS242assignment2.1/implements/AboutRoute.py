__author__ = 'shiwei'
import math

from implements import Query


"""
print the total distance, cost and time taken as
@param city_list dictionary[code:city]
@param searchForCode[city.name:code]
"""
def routeInformation(city_list, searchForCode):
    query = Query.Query(city_list, searchForCode)

    print("City List:")
    print_cities(query.get_all_city())
    valid = False
    while(not valid):
        print("Select a city as the departure or press q to go back:")
        input = raw_input()
        valid = input in searchForCode
        if(input == "q"):
            return


    code = searchForCode[input]
    start_city = city_list[code]
    city = start_city
    airports = [code]
    legs = []

    while(True):
        output = ""
        for destination in city.accessibleList:
            output += destination + ", "

        code = ""
        valid_code = False

        while(not valid_code):
            print("Please choose the next city or press 'return' button when you are done.")
            print(output)
            code = raw_input()
            valid_code = (code in city.accessibleList) or (code == "")

        if(code == ""):
            break
        legs.append(city.accessibleList[code])
        airports.append(code)
        city = city_list[code]

    print("Total Distance = " + str(calc_total_distance(legs)) )
    print("Total Cost = $" + str(calc_total_cost(legs)))
    print("Total Time = " + str(calc_total_time(legs, airports, city_list)) + " hours")



"""
calculate total distance
@param legs is a list of number which represent the distance for every leg of the journey
"""
def calc_total_distance(legs):
    sum = 0
    for i in legs:
        sum += i
    return sum

def calc_total_cost(legs):
    cost = legs[0] * .35

    for i in range(1, len(legs)):
        temp = .35-.05*i
        if temp < 0:
            temp=0
        cost += legs[i] * temp

    return cost


"""
@param the list keeps the distance of each leg of journey
@param airports is a list of city code on the trip
@param city_list the code the city dictionary
"""
def calc_total_time(legs, airports, city_list):
    totalTime = 0
    acceleration = 1406.25
    #750^2/2/200

    for i in range(len(legs)):
        if(legs[i] < 400):
            #x=0.5aT^2
            distance = legs[i]/2
            time = math.sqrt((2 * distance) / acceleration)
            totalTime += time * 2
        else:
            totalTime += math.sqrt((2 * 200) / acceleration)
            totalTime += math.sqrt((2 * 200) / acceleration)
            distance_static = legs[i] - 400
            totalTime += distance_static / 750
        #i=0 ,when #airport>2,wait
        if((i + 2) < len(airports)):
            #a outgoing plane means 10 mins off
            outbound = len(city_list[airports[i+1]].accessibleList)-1
            totalTime += 2 - outbound/6

    return totalTime



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

