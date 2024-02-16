# inputUser = input("masukan angka yang bernilai kurang dari 3 dan lebih dari 10 :")

# memeriksa angka kurang dari 3
inputUser = float(input("masukkan angka yang berbnilai kurang dari 3 :"))
kurangDari = (inputUser < 3)
print(kurangDari)

# > 10
lebihDari = inputUser > 10
print(lebihDari)

isCorect = kurangDari or lebihDari
print("angka yang anda masukkan: ", isCorect)
inputUser = float(input("masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 :"))

status = inputUser > 3 and inputUser < 10
print("hasilnya adalah : ", status)

#  EXERCISE
inputNumber = float(input("masukkan Angka > 0 dan < 5 atau > 8 dan < 11 :"))
hasil = (inputNumber > 0 and inputNumber < 5) or (inputNumber < 11 and inputNumber > 8)
print(" hasilnya adalah :", hasil)

# 2
inputUmber = float(input("masukkan angka < 0 atau >5 dan <8 atau >11 :"))
hasil1 = (inputUmber < 0) or (inputUmber > 5 and inputUmber < 8) or (inputUmber > 11)
print("hasil perbandingannya adalah ", hasil1)