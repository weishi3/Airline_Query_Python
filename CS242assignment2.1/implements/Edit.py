__author__ = 'shiwei'

import City
"""
remove a city and related routes
@:param city the city you want to delete
"""
def remove_city(city, city_list, searchForCode):
    city_code = searchForCode[city]
    del city_list[city_code]

    #city_list is the dict type (code,city)
    for i in city_list.itervalues():
        if(city_code in i.accessibleList):
            del i.accessibleList[city_code]


def add_city(code, name, country, continent, timezone, coordinates, population, region,code_indexed_cityList,searchForCode,link):
    city = City.City(code, name, country, continent, timezone, coordinates, population, region)


    code_indexed_cityList[city.code] = city

            # translate: city name->city code
    searchForCode[city.name] = code

    for i in link:
        city.accessibleList[i]=link[i]

'''
@param from_city the city the route start from
@param destination_code the city code of the route's destination
'''
def remove_route(from_city, destination_code):
    del from_city.accessibleList[destination_code]

'''
Given an Airport and the route information this will add the route into
the network.
@param from_city the city the route start from
@param destination_code the city code of the route's destination
'''
def add_route(from_city, destination_code, distance):
    from_city.accessibleList[destination_code] = distance

'''
This edits the city's Country

'''
def change_country(city, country):
    city.country = country

'''
This edits the city's Continent
'''
def change_continent(city, continent):
    city.continent = continent

'''
This edits the Airport's Timezone
'''
def change_timezone(city, timezone):
    city.timezone = timezone

'''
This edits the Airport's Region
'''
def change_region(city, region):
    city.region = region

'''
This edits the Airport's population
'''
def change_population(city, population):
    city.population = population