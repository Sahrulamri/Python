nama = "Rudi Setyawan"
formatStr = f"Hello {nama}"
print(formatStr)
# Angka
anga = 2005.87
format = f"Angka = {anga}"
print(format)

# bool
boolean = False
boole = f"Boolean = {boolean}"
print(boole)
# bilangan ribuan
angka = 3000
formatStr = f"jutaan = {angka:,}"
print(formatStr)
# bilangan desimal
angka = 3000.68698
formatStr = f"desimal = {angka:.3f}"
print(formatStr)

angka= 2555
formatBinary = f"binary = {bin(angka)}"
formatOctal = f"octal = {oct(angka)}"
formatHex = f"hex = {hex(angka)}"

print(formatBinary)
print(formatOctal)
print(formatHex)