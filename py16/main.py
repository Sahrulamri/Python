name = "Yang Mulia Raja Krab"
panjang = len(name)
print("panjang nama : ", panjang)

a = "a"
status = a in name
print("string ", a, " ada di ", name, " = ", status)
a = "f"
status = a not in name
print("string ", a, " ada di ", name, " = ", status)

# item paling kecil
print("Item paling kecil ", min(name))
# Item paling besar
print("Item paling besar ", max(name))

# ASCII
asciiCode = ord("b")
print("ASCII code untuk  spasi adalah ", str(asciiCode))
data = 117
print("Char untuk ASCII 117 adalah ", chr(data))

# operator method
data = "patrick lepaskan tanganmu"
jumlah = data.count("a")
print("jumlah o pada kata ", data , " = ", jumlah)
