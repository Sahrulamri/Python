# Latihan satuan temperatur

# Program konversi suhu

print("\n PROGRAM KONVERSI SUHU \n")

celcius = float(input("Masukkan suhu dalam selsius : "))

print("Suhu adalah", celcius, "Selsius")

# Reamur
reamur =  (4/5) * celcius
print("Suhu adalah ", reamur, "reamur");
# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu adalah ", fahrenheit, "fahrenheit")
# Kelvin
kelvin = celcius + 273
print("Suhu adalah ", kelvin, "kelvin")

# Reamur
reamur1 = float(input("Masukkan suhu dalam reamur : "))
print("Suhu adalah", reamur1, "Reamur")
# Celcius
celcius1 = (5/4) * reamur1
print("Suhu adalah ", celcius1, "celcius");
# Fahrenheit
fahrenheit1 = ((9/4) * reamur1)+32
print("Suhu adalah ", fahrenheit1, "fahrenheit");
# Kelvin
kelvin1 = ((5/4)*reamur1)+273
print("Suhu adalah ", kelvin1, "kelvin")

# FAHRENHEIT
fahrenheit2 = float(input("Masukkan suhu dalam fahrenheit : "))
print("Suhu adalah", fahrenheit2, "Fahrenheit")
# celcius
celcius2 = (5/9)*(fahrenheit2-32)
print("Suhu adalah ", celcius2, "celcius");
# Reamur
reamur2 = (4/9)* (fahrenheit2-32)
print("Suhu adalah", reamur2, "Reamur")
# Kelvin
kelvin2 = (5/9) *(fahrenheit2 - 32) + 273
print("Suhu adalah ", kelvin2, "kelvin")

# KELVIN
kelvin3 = float(input("Masukkan suhu dalam fahrenheit : "))
print("Suhu adalah", kelvin3, "Kelvin")
# celcius
celcius3 = kelvin3 - 273
print("Suhu adalah ", celcius3, "celcius");
# Reamur
reamur3 = (4/5) * (kelvin3 - 273)
print("Suhu adalah", reamur3, "Reamur")
# Fahrenheit
fahrenheit3 = (9/5) * (kelvin3-273) + 32
print("Suhu adalah ", fahrenheit3, "fahrenheit");









