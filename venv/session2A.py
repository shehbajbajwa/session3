johnsAge = 30
print(johnsAge,hex(id(johnsAge)))

jenniesAge = 30
print(jenniesAge,hex(id(jenniesAge)))
#hex code is same for both, id data is same then it will point at same location(reference pointers)

#copy operation, this is not data copy but reference copy
jacksAge = johnsAge
print(jacksAge,hex(id(jacksAge)))


#del johnsAge
#print(jenniesAge,hex(id(jenniesAge)))

# johnsage and jenniesage are known are reference variables.
