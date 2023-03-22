import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_maara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisella_edullinen(self):
        self.assertEqual((self.kassapaate.syo_edullisesti_kateisella(500)), 260)

    def test_kateisella_maukas(self):
        self.assertEqual((self.kassapaate.syo_maukkaasti_kateisella(500)), 100)

    def test_kassan_summa_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual((self.kassapaate.kassassa_rahaa), 100240)

    def test_kassan_summa_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual((self.kassapaate.kassassa_rahaa), 100400)

    def test_edullisten_maara_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(500)

        self.assertEqual((self.kassapaate.edulliset), 1)

    def test_maukkaat_maara_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_maksu_ei_riita_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)

    def test_rahat_takas_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_edulliset_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual((self.kassapaate.edulliset), 0)

    def test_maksu_ei_riita_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)

    def test_rahat_takas_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_maukkaat_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)

        self.assertEqual((self.kassapaate.maukkaat), 0)

    def test_kortilla_edullisesti(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual((self.kassapaate.edulliset), 1)

    def test_kortilla_maukkaasti(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_kortilla_ei_rahaa_edullinen(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual((self.maksukortti.saldo), 100)
        self.assertEqual((self.kassapaate.edulliset), 0)

    def test_kortilla_ei_rahaa_maukas(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((self.maksukortti.saldo), 100)
        self.assertEqual((self.kassapaate.maukkaat), 0)

    def test_ladataan_kortille_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 101000)
        self.assertEqual((self.maksukortti.saldo), 2000)

    def test_ladataan_kortille_rahaa_neg(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)
        self.assertEqual((self.maksukortti.saldo), 1000)
