salam = "Hallo"
salam = salam.upper()
print(salam)

alay = "Ini Itu Tidak Ada Gunanya"
alay = alay.lower()
print(alay)
# Pengecekan
salam = "hallo"
lower = salam.islower()
print(lower)
salam = "hallo"
lower = salam.isupper()
print(lower)
judul = "Hari Ini Hari Apaya"
cekJudul = judul.istitle()
print("Judul ,", cekJudul)
# mengecek komponen
cekstart = "Ini keren sekali".startswith("Ini")
print("start = ", cekstart)
cekstart = "Ini keren sekali".endswith("Ini")
print("start = ", cekstart)

buah = ["jeruk", "apel", "mangga", "alpukat"]
gaabung = ','.join(buah)
print(buah)
print(gaabung)

gabung = ' '.join(buah)
print(gabung)
gabungan = "halo,selamat,pagi"
print(gabungan.split(','))