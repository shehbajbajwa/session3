ages1 = (10, 20, 30, 40, 50, 60, 30)
ages2 = [10, 20, 30, 40, 50, 60, 30]
ages3 = {10, 20, 30, 40, 50, 60, 30}

print(ages1, hex(id(ages1)), type(ages1))
print(ages2, hex(id(ages2)), type(ages2))
print(ages3, hex(id(ages3)), type(ages3))

#in my program i cannot change the content of tuple
#hence it is IMMUTABLE
#list is MUTABLE
#set is MUTABLE  and UnOrdered due to uniqueness

#how to read in set...
for x in ages3:
    print(x,hex(id(x)))