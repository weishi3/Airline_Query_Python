__author__ = 'shiwei'


class Query:




    def __init__(self, city_list, searchForCode):
        self.city_list = city_list
        self.searchForCode = searchForCode

    """
    return all cities names for query
    """

    #all city name:part 1
    def get_all_city(self):
        all_city = []
        for i in self.city_list:
            city = self.city_list[i]
            all_city.append(city.name)

        return all_city

    #basic queries:part2
    """
    given the name of a city, get the city code
    """
    def get_city_code(self, city_name):
        return self.searchForCode[city_name]


    """
    return the country the given city_name belongs to
    """
    def get_country(self, city_name):
        return self.city_list[self.searchForCode[city_name]].country

    """
    return the continent the given city_name belongs to
    """
    def get_continent(self, city_name):
        return self.city_list[self.searchForCode[city_name]].continent
    """
    return the timezone the given city_name belongs to
    """
    def get_timezone(self, city_name):
        return self.city_list[self.searchForCode[city_name]].timezone
    """
    return the coordinate the given city_name belongs to
    """
    def get_coordinates(self, city_name):
        return self.city_list[self.searchForCode[city_name]].coordinates
    """
    return the population of the city with given city_name
    """
    def get_population(self, city_name):
        return self.city_list[self.searchForCode[city_name]].population
    """
    return the region of the city with given city_name
    """
    def get_region(self, city_name):
        return self.city_list[self.searchForCode[city_name]].region


    """
    return the deep copy of accessibleList of a city
    """
    def get_accessible_list(self, city):
        accessible_list = city.accessibleList
        accessible_list_copy = []
        for i in accessible_list.keys():
            accessible_list_copy.append((self.city_list[i].name,accessible_list[i]))

        return accessible_list_copy

    """
    return the tuple[from, to ,distance] of the longest flight
    """
    def get_longest_flight(self):
        max_distance = 0
        the_flight = []

        # search through each city and outgoing routes for the longest
        for i in self.city_list:
            city = self.city_list[i]

            for code in city.accessibleList.keys():
                if city.accessibleList[code] > max_distance:
                    max_distance = city.accessibleList[code]
                    the_flight = [city.name, self.city_list[code].name, max_distance]

        return the_flight


    """
    return the tuple[from, to ,distance] of the shortest flight
    """
    def get_shortest_flight(self):
        min_distance = -1
        the_flight = []

        # search through each city and outgoing routes for the longest
        for i in self.city_list:
            city = self.city_list[i]

            for code in city.accessibleList:

                if min_distance == -1:
                    min_distance = city.accessibleList[code]
                    the_flight = [city.name, self.city_list[code].name, min_distance]
                elif city.accessibleList[code] < min_distance:
                    min_distance = city.accessibleList[code]
                    the_flight = [city.name, self.city_list[code].name, min_distance]

        return the_flight


    """
    return the average distance of all flights
    """
    def get_average_distance(self):
        whole = 0
        count = 0
        # search through each city and outgoing routes for the longest
        for i in self.city_list:
            city = self.city_list[i]

            for code in city.accessibleList.keys():
                whole += city.accessibleList[code]
                count += 1

        return whole / count

    """
    return [city.name, population] of the largest city
    """
    def get_biggest_city(self):
        population = 0
        biggest_city = []

        # search through each city and outgoing routes for the longest
        for i in self.city_list:
            city = self.city_list[i]

            if city.population > population:
                    population = city.population
                    biggest_city = [city.name, population]

        return biggest_city


    """
    return [city.name, population] of the smallest city
    """
    def get_smallest_city(self):
        population = -1
        smallest_city = []

        # search through each city and outgoing routes for the longest
        for i in self.city_list:
            city = self.city_list[i]
            if population == -1 or city.population < population:
                population = city.population
                smallest_city = [city.name, population]

        return smallest_city

    """
    return the average population of all cities
    """
    def get_average_size(self):
        whole = 0
        count = 0

        for i in self.city_list:
            city = self.city_list[i]
            whole += city.population
            count += 1

        return whole / count

    """
    return a list of continents and the cities belonging to them
    """
    def get_continent_list(self):
        continent_list = {}

        for i in self.city_list:
            city = self.city_list[i]
            if( not (city.continent in continent_list)):
                continent_list[city.continent] = [city.name]
            else:
                continent_list[city.continent].append(city.name)

        return continent_list
    """
    The old version:
    def get_hub_city(self):
        city_list = []
        temp = 0
        for i in self.city_list:
            print(i)
            city = self.city_list[i]
            if len(city.accessibleList) > temp:
                city_list = [city.name]
                temp = len(city.accessibleList)
            elif len(city.accessibleList) == temp:
                city_list.append(city.name)

        return city_list

    """


    """
    return the cities with most connections
    """
    def get_hub_city(self):
        city_list = []
        temp = {}
        for i in self.city_list:
            city = self.city_list[i]
            temp[city.name] = len(city.accessibleList)
        for i in self.city_list:
            for j in self.city_list[i].accessibleList:
                city = self.city_list[j]
                temp[city.name] += 1
        max_link = 0
        for i in temp:
            if temp[i] > max_link:
                city_list = [i]
                max_link = temp[i]
            elif temp[i] == max_link:
                city_list.append(i)
        return city_list

