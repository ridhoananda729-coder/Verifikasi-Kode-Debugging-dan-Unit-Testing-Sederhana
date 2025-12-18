import unittest
from diskon_service import DiskonCalculator

class TestDiskonLanjut(unittest.TestCase): # Sesuai instruksi 3a 
    
    def setUp(self):
        """Arrange: Siapkan instance Calculator."""
        self.calc = DiskonCalculator()

    def test_diskon_standar(self):
        """Uji diskon 10%."""
        self.assertEqual(self.calc.hitung_diskon(1000, 10), 900.0)

    # Tes 5: Uji nilai float (Instruksi 3b) [cite: 191]
    def test_nilai_float(self):
        """Uji nilai float (diskon 33% pada 999)."""
        hasil = self.calc.hitung_diskon(999, 33)
        # Menggunakan assertAlmostEqual sesuai perintah [cite: 192]
        self.assertAlmostEqual(hasil, 669.33, places=2)

    # Tes 6: Uji Edge Case (Instruksi 3b) [cite: 194]
    def test_edge_case_harga_nol(self):
        """Uji Edge Case (harga awal 0)."""
        self.assertEqual(self.calc.hitung_diskon(0, 10), 0.0)

if __name__ == '__main__':
    unittest.main()