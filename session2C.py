dishPrice = 100

dishesPrices = 100, 200, 350, 500, 120 #homogenous
#print(dishPrice, hex(id(dishPrice)), type(dishPrice))

anotherDishesPrices = 100, 200.22, 350, 500, 120, "100"  #heterogenous

#class is a root of classification
print(dishesPrices, hex(id(dishesPrices)), type(dishesPrices))

print(dishesPrices[0], hex(id(dishesPrices[0])), type(dishesPrices[0]))
print(anotherDishesPrices[0], hex(id(anotherDishesPrices[0])), type(anotherDishesPrices[0]))