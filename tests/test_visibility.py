import unittest
import metar_tools

report1 = 'EGUW 110550Z AUTO 05012KT 3000 OVC120/// 02/01 Q0980='

report2 = 'SPECI EGXE 210910Z 12005KT 9999 3000SW BR FEW003 SCT021 ' \
           'BKN070 10/10 Q1005 YLO1 BECMG 24015KT 9999 NSW SCT010 GRN='

report3 = 'EGSS 040820Z 25002KT 3000 2000SW R22/1000 FG BR BCFG' \
          'NSC 01/01 Q1032='

report4 = 'KJFK 070651Z 26013KT 6SM SCT070 BKN250 05/M04 A3001 RMK A ' \
         'O2 SLP161 T00501039='

report5 = 'EGVO 120550Z 24005KT CAVOK M03/M04 Q1005 BLU='

report6 = 'EGLL 120550Z AUTO 28004KT 9000 NCD M03/M05 Q1005 NOSIG= '


class TestVisibilityDecode(unittest.TestCase):
    def test_vis_metres_auto(self):
        vis = metar_tools.get_vis_fm_mtrs(report1)
        self.assertEqual(vis, 3000)

    def test_vis_directional(self):
        vis = metar_tools.get_vis_fm_mtrs(report2)
        self.assertEqual(vis, 3000)

    def test_vis_runway(self):
        vis = metar_tools.get_vis_fm_mtrs(report3)
        self.assertEqual(vis, 1000)

    def test_vis_cavok(self):
        vis = metar_tools.get_vis_fm_mtrs(report5)
        self.assertEqual(vis, 9999)

    def test_vis_miles(self):
        vis = metar_tools.get_vis_fm_mtrs(report4)
        self.assertEqual(vis, 9678)


if __name__ == '__main__':
    unittest.main()
