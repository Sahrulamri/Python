a =9
b =5
# 0r
c = a | b
print('nilai : ', a, ' binary : ', format(a,'08b'))
print('nilai : ', b, ' binary : ', format(b,'08b'))
print('nilai : ', c, ' binary : ', format(c,'08b'))
print("nilai", c)
# and
c = a & b
print('nilai : ', a, ' binary : ', format(a,'08b'))
print('nilai : ', b, ' binary : ', format(b,'08b'))
print('nilai : ', c, ' binary : ', format(c,'08b'))
print("nilai", c)
# xor
c = a ^ b
print('nilai : ', a, ' binary : ', format(a,'08b'))
print('nilai : ', b, ' binary : ', format(b,'08b'))
print('nilai : ', c, ' binary : ', format(c,'08b'))
print("nilai", c)
# not
c = ~a
print("============================NOT")
print("nilai a = ", a, ' binary  :', format(a, '08b'))
print("-------------------------------------( ~)")
print('nilai : ', c ,' binary :', format(c,  '08b'))
print("--------------------------------- ( ^ )")
d = 0b0000001001
e = 0b1111111111
print('nilai : ', e ^ d, ' , binary :', format(e^d, '08b'))
# Shift Rigth
c = a >> 2
print("============================>>")
print("nilai a = ", a, ' binary  :', format(a, '08b'))
print("-------------------------------------( >>)")
print('nilai : ', c ,' binary :', format(c,  '08b'))
# Shift Left
c = a << 2
print("=========================== <<")
print("nilai a = ", a, ' binary  :', format(a, '08b'))
print("-------------------------------------( << )")
print('nilai : ', c ,' binary :', format(c,  '08b'))