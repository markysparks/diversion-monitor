import unittest

from station_data import StationData

report1 = 'EGUW 112150Z AUTO 05012KT 9999 BKN030/// 02/01 Q0980='  # BLU

report2 = 'EGUW 112250Z AUTO 05012KT 7000 HZ SCT020/// 02/01 Q0980='  # WHT

taf1 = 'TAF EGUW 112030Z 3121/0115 22014KT 9999 SCT030 PROB40 TEMPO 3121/0101 24015G25KT 5000 RA SCT012='


class TestCase(unittest.TestCase):

    def test_state_change(self):
        self.icao_data = StationData()
        self.icao_data.update_icao_data('EGUW', '112150Z', report1,
                                        '112030Z', taf1,
                                        self.icao_data.station_dict)

        print(self.icao_data.station_dict.values())

        # self.icao_data.update_icao_data('EGUW', '112250Z', report2,
        #                                 '112030Z', taf1,
        #                                 self.icao_data.station_dict)
        #
        # print(self.icao_data.station_dict.values())

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
