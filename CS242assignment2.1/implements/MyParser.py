__author__ = "shiwei"

import json

from implements import City


"""
It parse file to database, or save data to file
"""
class MyParser():
    # @param sourcefile: the data file in json used as the source to parse
    def __init__(self, sourcefile):
        self.sourcefile = sourcefile
        self.code_indexed_cityList = {}
        self.searchForCode = {}
    
    """
    use this function to initial the database or parse a new file
    @param when new="init", it means the original state
        otherwise, new= new file name
    """
    def parse(self,new):
        if new == "init":
            jsondata = json.load(open(self.sourcefile))
        else:
            jsondata = json.load(open(new))
        
        # parse through the city information
        for metro in jsondata["metros"]:
            code = metro["code"]
            name = metro["name"]
            country = metro["country"]
            continent = metro["continent"]
            timezone = metro["timezone"]
            coordinates = metro["coordinates"]
            population = metro["population"]
            region = metro["region"]
            
            # Creat the city object with its own factors
            city = City.City(code, name, country, continent, timezone, coordinates, population, region)
            
            # translate: code->city object
            self.code_indexed_cityList[city.code] = city

            # translate: city name->city code
            self.searchForCode[city.name] = code
        
        # record the j of each route (saved as code) and use code as a index to keep distance data
        # struture: (code, distance) pair in a list
        for route in jsondata["routes"]:    
            departure_code = route["ports"][0]
            j_code = route["ports"][1]
            distance = route["distance"]
            self.code_indexed_cityList[departure_code].accessibleList[j_code] = distance

    '''
    It will write to a file named by filename in the JSON format
    '''
    def save_disk(self,filename):
        root = {}
        metros = []
        routes = []
        
        # i in type city
        for i in self.code_indexed_cityList.itervalues():
            city_dict = {}
            city_dict["code"] = i.code
            city_dict["name"] = i.name
            city_dict["country"] = i.country
            city_dict["continent"] = i.continent
            city_dict["timezone"] = i.timezone
            city_dict["coordinates"] = i.coordinates
            city_dict["population"] = i.population
            city_dict["region"] = i.region
            
            metros.append(city_dict)
            
            # j is the target of accessibleList
            for j in i.accessibleList:
                distance = i.accessibleList[j]
                route_dic = {}
                #code
                route_dic["ports"] = [i.code, j]
                route_dic["distance"] = distance
                routes.append(route_dic)
            
        root["metros"] = metros
        root["routes"] = routes

        # Write the JSON output to the file
        new_file = open(filename, "w")
        new_file.write(json.dumps(root))