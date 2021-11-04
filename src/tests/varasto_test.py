import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        omavarasto = Varasto(-10)
        self.assertAlmostEqual(omavarasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollataan(self):
        omavarasto = Varasto(10, -5)
        self.assertAlmostEqual(omavarasto.saldo, 0)

    def test_negatiivinen_lisays_varastoon_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_varastoon_ei_voi_lisata_enemman_kuin_tilavuus(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_tyhjasta_varastosta_ei_voi_ottaa_mitaan(self):
        saatu = self.varasto.ota_varastosta(5)
        self.assertAlmostEqual(saatu, 0)
    
    def test_varastosta_ei_voi_ottaa_enemman_kuin_siina_on(self):
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(saatu, 5)
    
    def test_varastosta_ei_voi_ottaa_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_varasto_tulostuu_oikein(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 1000, vielä tilaa 10" )
