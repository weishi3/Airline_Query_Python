__author__ = 'shiwei'
import copy

from implements import Query


"""
a help function to print 16 cities in a line
"""
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
find the shortest path
@param city_list : a code to city dictionary
@param searchForCode: a name to code dictionary
print distance and the path in code
"""
def findShortestRoute(city_list, searchForCode):
    
    query = Query.Query(city_list, searchForCode)
    start = ""
    end = ""
    
    print("City List:")
    print_cities(query.get_all_city())
    valid_city = False
    while not valid_city:
        print("Select a city as the departure or press q to go back:")
        start = raw_input()
        valid_city = start in searchForCode
        if start == "q":
            return
    
    valid_city = False
    while not valid_city:
        print("Select a city as the destination or press q to go back:")
        end = raw_input()
        valid_city = end in searchForCode
        if start == "q":
            return
    start = searchForCode[start]
    end = searchForCode[end]


    dist={}
    dist[(start,start)]=0
    path={}
    for i in city_list:
        if i != start:
            dist[(start,i)]=99999999999999
        path[i]=[]
    S=[]
    path[start].append(start)
    for i in range(len(city_list)):
        temp=(99999999999999,"")
        for j in city_list:
            if j not in S:
                if dist[(start,j)]<temp[0]:
                    temp=(dist[(start,j)],j)
        dist[(start,temp[1])] = temp[0]
        S.append(temp[1])
        #path[temp[1]].append(temp[1])
        if temp[1]!="":
            for u in city_list[temp[1]].accessibleList:
                if dist[(start, u)]< (dist[(start, temp[1])] + city_list[temp[1]].accessibleList[u]):
                    path[u] = path[u]
                else:
                    path[u]=copy.deepcopy(path[temp[1]])
                    path[u].append(u)
                dist[(start, u)] = min(dist[(start, u)], dist[(start, temp[1])] + city_list[temp[1]].accessibleList[u])


    print dist[(start, end)]
    print_cities(path[end])

