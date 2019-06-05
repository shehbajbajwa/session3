#bitwise operators

a = 8     #1000
b = 12    #1100
c = a & b #1000
d = a | b #1100 #or
e = a ^ b #0100 #exor


print(c)
print(d)
print(e)

"""
x = 12 #1100
y = 3
z= x >> y # right shift operation
# 1100 >> 3 -> 0 0 0 1
z = x << y # 1100 << 3 -> 1100 000 
print(z)
"""

x = -11 #1011
y = 2  #0010
z = x >> y
print(z)

# 1011
#0100 1s comp
#0101 2s comp
# _ _ 01 shift by 2
# 1101 coz the number is negative
#0010  1s
#0011  2s -> -3