import pdb

class DiskonCalculator:
    """Menghitung harga akhir setelah diskon."""
    def hitung_diskon(self, harga_awal: float, persentase_diskon: int) -> float:
        # Perbaikan bug pertama: persentase harus dibagi 100 [cite: 109]
        jumlah_diskon = harga_awal * persentase_diskon / 100 
        
        # --- SIMULASI BUG BARU (Tugas Mandiri) ---
        # Menambahkan PPN 10% secara tidak sengaja 
        # Hapus baris di bawah ini nanti setelah proses debug selesai
        harga_akhir = (harga_awal - jumlah_diskon) * 1.1 
        
        return harga_akhir

if __name__ == '__main__':
    calc = DiskonCalculator()
    # Untuk laporan debug: aktifkan baris di bawah ini dan gunakan perintah 'p' 
    # pdb.set_trace() 
    hasil = calc.hitung_diskon(1000, 10)
    print(f"Hasil (Masih ada Bug PPN): {hasil}")