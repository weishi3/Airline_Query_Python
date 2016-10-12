__author__ = 'shiwei'

import unittest

from implements import MyParser,Query,Edit




# I build some virtual cities to test:
class MyTestCase(unittest.TestCase):

    def test_WAR3(self):
        #test parsers
        ui_parser = MyParser.MyParser("warcraft3_city.txt")
        ui_parser.parse("init")
        the_query = Query.Query(ui_parser.code_indexed_cityList, ui_parser.searchForCode)

        #note: i is the city name here
        for i in the_query.get_all_city():
            #test query helper function
            if the_query.get_city_code(i) == "CAPH":
                #test basic queries
                self.assertEqual(the_query.get_country(i), "Human")
                self.assertEqual(the_query.get_continent(i), "Lordaeron")
                self.assertEqual(the_query.get_timezone(i), -3)
                self.assertEqual(the_query.get_population(i), 60000000000)
                self.assertEqual(the_query.get_region(i), 1)
                j=the_query.get_accessible_list(ui_parser.code_indexed_cityList[ui_parser.searchForCode[i]])
                print j

                self.assertEqual(ui_parser.code_indexed_cityList["CAPU"].name, "UnderCity")

            else:
                k=the_query.get_accessible_list(ui_parser.code_indexed_cityList[ui_parser.searchForCode[i]])
                print k

                self.assertEqual(the_query.get_region(i), 2)

        #test advance functions
        self.assertEqual(the_query.get_average_distance(),2453)
        self.assertEqual(the_query.get_smallest_city()[0],"UnderCity")
        #(4000000+6000000)/2=5000000
        self.assertEqual(the_query.get_average_size(), 30002000000)
        self.assertEqual(the_query.get_continent_list(), {u'Lordaeron': [u'UnderCity', u'Dalaran']})
        self.assertEqual(the_query.get_longest_flight(),the_query.get_shortest_flight())
        self.assertEqual(the_query.get_hub_city(),[u'UnderCity', u'Dalaran'])


        ui_parser.parse("myData.txt")
        the_query = Query.Query(ui_parser.code_indexed_cityList, ui_parser.searchForCode)

        #no longer [u'UnderCity', u'Dalaran']
        self.assertEqual(the_query.get_hub_city(),[u'Istanbul', u'Hong Kong'])

        # but the biggest city is still the magic Dalaran
        self.assertEqual(the_query.get_biggest_city(),[u'Dalaran', 60000000000])

        # after Arthas coming
        Edit.change_population(ui_parser.code_indexed_cityList[ui_parser.searchForCode[u'Dalaran']],60)
        self.assertEqual(the_query.get_biggest_city(),[u'Tokyo', 34000000])

        Edit.add_route(ui_parser.code_indexed_cityList["PAR"],"CAPH",1000000);
        self.assertEqual(ui_parser.code_indexed_cityList["PAR"].accessibleList["CAPH"],1000000)
        self.assertEqual(ui_parser.code_indexed_cityList["PAR"].accessibleList[ui_parser.searchForCode["Essen"]],433)



        ui_parser.save_disk("modifies_war.json")

if __name__ == '__main__':
    unittest.main()
