"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sequential: langkah berututan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah  yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sequential
print('Ibu berkata,"Pergi ke toko"')
print('Anak menjawab,"Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab,"Beli satu botol susu, dan jika ada telur beli 6"')
print("Maka anak berangkat ke toko")
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Anak mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 1 botol susu dan 6 buah telur")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada ibu")
