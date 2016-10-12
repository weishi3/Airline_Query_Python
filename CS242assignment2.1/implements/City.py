__author__ = 'shiwei'


class City:
    # data structure dealing with "node"
    # "edge" would be expressed as instance variable "accessibleList"

    # constuctor of city as nodes
    def __init__(self, code, name, country, continent, timezone, coordinates, population, region):

        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population
        self.region = region
        #accessibleList would contain some (code,distance)
        self.accessibleList = {}