import unittest
import metar_tools

report1 = 'EGUW 110550Z AUTO 05012KT 8000 OVC120/// 02/01 Q0980='

report2 = 'SPECI EGXE 210910Z 12005KT 9999 3000SW BR FEW003 SCT021 ' \
           'BKN070 10/10 Q1005 YLO1 BECMG 24015KT 9999 NSW SCT010 GRN='

report3 = 'EGSS 040820Z 25002KT 3000 2000SW R22/0450 FG BR BCFG' \
          'NSC 01/01 Q1032='

report4 = 'KJFK 070651Z 26013KT 6SM BKN004 05/M04 A3001 RMK A ' \
         'O2 SLP161 T00501039='

report5 = 'EGVO 120550Z 24005KT CAVOK M03/M04 Q1005 BLU BECMG 4000 BR GRN'

report6 = 'EGLL 120550Z AUTO 28004KT 7000 NCD M03/M05 Q1005 NOSIG= '

report7 = 'EGUW 110550Z AUTO 05012KT 1200 OVC002/// 02/01 Q0980='

report8 = 'EGUW 110550Z AUTO 05012KT 4000 OVC007/// 02/01 Q0980='

report9 = 'EGUW 110550Z AUTO 05012KT 7000 OVC015/// 02/01 Q0980='


class TestVisibilityDecode(unittest.TestCase):

    def test_vis_metres_auto(self):
        vis = metar_tools.get_vis_fm_mtrs(report1)
        self.assertEqual(vis, 8000)

    def test_vis_directional(self):
        vis = metar_tools.get_vis_fm_mtrs(report2)
        self.assertEqual(vis, 3000)

    def test_vis_runway(self):
        vis = metar_tools.get_vis_fm_mtrs(report3)
        self.assertEqual(vis, 450)

    def test_vis_miles(self):
        vis = metar_tools.get_vis_fm_mtrs(report4)
        self.assertEqual(vis, 9678)

    def test_vis_cavok(self):
        vis = metar_tools.get_vis_fm_mtrs(report5)
        self.assertEqual(vis, 9999)

    def test_vis_ncd(self):
        vis = metar_tools.get_vis_fm_mtrs(report6)
        self.assertEqual(vis, 7000)


class TestCloudDecode(unittest.TestCase):

    def test_cloud_ovc(self):
        base = metar_tools.get_sig_cloud_height(report1)
        self.assertEqual(base, 12000)

    def test_cloud_sct(self):
        base = metar_tools.get_sig_cloud_height(report2)
        self.assertEqual(base, 2100)

    def test_cloud_nsc(self):
        base = metar_tools.get_sig_cloud_height(report3)
        self.assertEqual(base, 2500)

    def test_cloud_bkn(self):
        base = metar_tools.get_sig_cloud_height(report4)
        self.assertEqual(base, 400)

    def test_cloud_cavok(self):
        base = metar_tools.get_sig_cloud_height(report5)
        self.assertEqual(base, 2500)

    def test_cloud_ncd(self):
        base = metar_tools.get_sig_cloud_height(report6)
        self.assertEqual(base, 2500)


class TestColourState(unittest.TestCase):

    def test_RED(self):
        colour = metar_tools.get_colourstate_nbr(report3)
        self.assertEqual(colour, 1)

    def test_AMB(self):
        colour = metar_tools.get_colourstate_nbr(report7)
        self.assertEqual(colour, 2)

    def test_YL02(self):
        colour = metar_tools.get_colourstate_nbr(report4)
        self.assertEqual(colour, 3)

    def test_YL01(self):
        colour = metar_tools.get_colourstate_nbr(report2)
        self.assertEqual(colour, 4)

    def test_GRN(self):
        colour = metar_tools.get_colourstate_nbr(report8)
        self.assertEqual(colour, 5)

    def test_WHT(self):
        colour = metar_tools.get_colourstate_nbr(report9)
        self.assertEqual(colour, 6)

    def test_BLU(self):
        colour = metar_tools.get_colourstate_nbr(report1)
        self.assertEqual(colour, 7)

    def test_NCD(self):
        colour = metar_tools.get_colourstate_nbr(report6)
        self.assertEqual(colour, 6)

    def test_CAVOK(self):
        colour = metar_tools.get_colourstate_nbr(report5)
        self.assertEqual(colour, 7)


if __name__ == '__main__':
    unittest.main()
