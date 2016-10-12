__author__ = 'shiwei'

import unittest

from implements import MyParser, UI_interface
import UI_interface


class MyTestCase(unittest.TestCase):
    #test for the given CSAIR DATA
    #test for correct url
    def test_option2(self):
        ui_parser = MyParser.MyParser("myData.txt")
        ui_parser.parse()
        tester= UI_interface.openMap(ui_parser.code_indexed_cityList, ui_parser.searchForCode)

        self.assertEqual(tester,"http://www.gcmap.com/mapui?P=PAR-ESS,+PAR-MIL,+MIL-ESS,+MIL-IST,+MIA-WAS,+CCU-HKG,+CCU-BKK,+LIM-MEX,+LIM-BOG,+ATL-MIA,+ATL-WAS,+PEK-ICN,+LON-NYC,+LON-PAR,+LON-ESS,+IST-BGW,+LOS-FIH,+LOS-KRT,+CAI-ALG,+CAI-RUH,+CAI-BGW,+CAI-IST,+DEL-CCU,+DEL-MAA,+DEL-BOM,+BOM-MAA,+BGW-KHI,+BGW-RUH,+BGW-THR,+NYC-YYZ,+BOG-MIA,+BOG-SAO,+BOG-BUE,+SCL-LIM,+SAO-LOS,+SAO-MAD,+SFO-CHI,+JKT-SYD,+BKK-JKT,+BKK-HKG,+BKK-SGN,+KHI-DEL,+KHI-BOM,+MNL-SFO,+MNL-SGN,+MNL-SYD,+SGN-JKT,+OSA-TPE,+HKG-SHA,+HKG-TPE,+HKG-MNL,+HKG-SGN,+BUE-SAO,+TPE-MNL,+ESS-LED,+ICN-TYO,+CHI-ATL,+CHI-YYZ,+THR-KHI,+THR-RUH,+THR-DEL,+KRT-CAI,+SHA-TPE,+SHA-TYO,+SHA-ICN,+SHA-PEK,+FIH-JNB,+FIH-KRT,+WAS-NYC,+WAS-YYZ,+RUH-KHI,+TYO-OSA,+TYO-SFO,+LED-MOW,+LED-IST,+SYD-LAX,+ALG-PAR,+ALG-MAD,+ALG-IST,+MOW-THR,+MOW-IST,+MAA-CCU,+MAA-JKT,+MAA-BKK,+JNB-KRT,+LAX-SFO,+LAX-CHI,+MAD-NYC,+MAD-PAR,+MAD-LON,+MEX-MIA,+MEX-CHI,+MEX-LAX,+MEX-BOG")

    #test for
if __name__ == '__main__':
    unittest.main()
